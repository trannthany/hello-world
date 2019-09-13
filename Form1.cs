using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
namespace Hangman_V5
{
    public partial class FormHangman : System.Windows.Forms.Form
    {
        #region Constant value fields
        const int NUM_BUTTONS = 26;
        const int NUM_COLS = 9;
        const int BTN_WIDTH = 25;
        const int BTN_HEIGTH = 25;
        const int LEFT_MARGIN = 530;
        const int TOP_MARGIN = 155;
        const int HOZ_GAP = 15;
        const int VER_GAP = 15;
        List<Button> buttons = new List<Button>();
        #endregion
        #region Global Variables
        private int wrongCount = 0;
        private string word;
        private bool isWin = false;
        List<Label> labels = new List<Label>();
        Stopwatch sw = Stopwatch.StartNew();
        #endregion
        enum BodyParts
        {
            Head,
            Left_Eye,
            Right_Eye,
            Mouth,
            Body,
            Right_Arm,
            Left_Arm,
            Right_Leg,
            Left_Leg,
            p
        }
        public FormHangman()
        {
            InitializeComponent();
        }

        private void ButtonClose_Click(object sender, EventArgs e)
        {
            this.Close();
            timer.Stop();
        }

        private void ButtonSubmitWord_Click(object sender, EventArgs e)
        {
            
            if (textBoxWord.Text.ToLower() == word)
            {
                YouWin();
            }
            else
            {
                wrongCount++;
                Draw();
                ShowPictures();
                if (wrongCount == 9) YouLose();
            }
        }
        
        private void FormHangman_Load(object sender, EventArgs e)
        {
            this.CenterToScreen();
            MakeLabels();
            LoadButtons();
            timer.Start();
            //Stopwatch sw = Stopwatch.StartNew();
            //labelTime.Text = sw.Elapsed.ToString();

        }
        private void Panel1_Paint(object sender, PaintEventArgs e)
        {
            DrawHangmanPost();
            Draw();
           
        }
        #region button making
        private void LoadButtons()
        {
            for (int i = 0; i < NUM_BUTTONS; i++)
            {
                Button btn = new Button();
                buttons.Add(btn);
                btn.Size = new Size(BTN_WIDTH, BTN_HEIGTH);

                //Laying out buttons
                int row = i / NUM_COLS;
                int col = i % NUM_COLS;
                btn.Location = new Point(col * (BTN_WIDTH + HOZ_GAP) + LEFT_MARGIN, row * (BTN_HEIGTH + VER_GAP) + TOP_MARGIN);

                //Labels each button
                char letter = (char)(i + 65);
                btn.Text = letter.ToString();

                //set the events
                btn.Click += Btn_Click;
                btn.TabStop = false;
                this.Controls.Add(btn);

            }
        }
        private void Btn_Click(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            btn.Enabled = false;
            char c = char.Parse(btn.Text.ToLower());
            CheckChar(c);                  
        }

        #endregion
        /*
        private void FormHangman_KeyPress(object sender, KeyPressEventArgs e)
        {
            char letter = char.ToUpper(e.KeyChar);
            e.Handled = true;
            buttons[letter - 65].Enabled = false;
        }
        */
        #region Support Classes
        private void MakeLabels()
        {
            word = GetRandomWord();
            char[] chars = word.ToCharArray();
            int between = 450 / chars.Length;
            for (int i = 0; i < chars.Length; i++)
            {
                labels.Add(new Label());
                labels[i].Location = new Point((i * between) + 10, 80);
                labels[i].Text = "*";
                labels[i].Font = new Font("Comic Sans MS", 12);
                labels[i].Parent = groupBoxButtons;
                labels[i].BringToFront();//bring the label on the top other controls
                labels[i].CreateControl();//create the control and show it on the form
            }
            labelWordLength.Text = "Word Length: " + word.Length.ToString();
            labelWrong.Text = "Wrong " + wrongCount.ToString();

        }

        private string GetRandomWord()
        {
            List<string> words = Words_Load();
            words.Sort();
            Random random = new Random();
            int num = random.Next(0, words.Count - 1);
            textBoxWord.MaxLength = words[num].Length;
            return words[num];
        }
        public static List<string> Words_Load()
        {
            List<string> words = new List<string>();
            using (StreamReader reader = new StreamReader(@"E:/data/random_words.txt"))
            {
                while (!reader.EndOfStream)
                {
                    words.Add(reader.ReadLine());
                }
                reader.Close();
            }

            return words;
        }

        private void DrawHangmanPost()
        {
            Graphics g = panel1.CreateGraphics();
            Pen p = new Pen(Color.Brown, 10);
            //hang post
            g.DrawLine(p, new Point(218, 223), new Point(5, 223));//base
            g.DrawLine(p, new Point(155, 218), new Point(155, 5));//pole
            g.DrawLine(p, new Point(390 / 2, 5), new Point(150, 5));//bar
            g.DrawLine(p, new Point(390 / 2, 0), new Point(390 / 2, 50));//rope
        }
        private void DrawBodyPart(BodyParts bp)
        {
            Graphics g = panel1.CreateGraphics();
            Pen p = new Pen(Color.Blue, 2);
            switch (bp)
            {
                case BodyParts.Head:
                    g.DrawEllipse(p, 390 / 2 - 20, 50, 40, 40);
                    break;
                case BodyParts.Left_Eye:
                    SolidBrush s = new SolidBrush(Color.Black);
                    g.FillEllipse(s, 390 / 2 - 10, 60, 5, 5);
                    break;
                case BodyParts.Right_Eye:
                    SolidBrush t = new SolidBrush(Color.Black);
                    g.FillEllipse(t, 390 / 2 + 5, 60, 5, 5);
                    break;
                case BodyParts.Mouth:
                    if (isWin)
                        g.DrawArc(p, 390 / 2 - 10, 60, 20, 20, 45, 90);
                    else
                        g.DrawArc(p, 390 / 2 - 10, 70, 20, 20, -45, -90);
                    break;
                case BodyParts.Body:
                    g.DrawLine(p, new Point(390 / 2, 90), new Point(390 / 2, 130));
                    break;
                case BodyParts.Left_Arm:
                    if (isWin)
                        g.DrawLine(p, new Point(390 / 2, 100), new Point(390 / 2 - 25, 80));
                    else
                        g.DrawLine(p, new Point(390 / 2, 100), new Point(390 / 2 - 25, 120));
                    break;
                case BodyParts.Right_Arm:
                    if (isWin)
                        g.DrawLine(p, new Point(390 / 2, 100), new Point(390 / 2 + 25, 80));
                    else
                        g.DrawLine(p, new Point(390 / 2, 100), new Point(390 / 2 + 25, 120));
                    break;
                case BodyParts.Left_Leg:
                    g.DrawLine(p, new Point(390 / 2, 130), new Point(390 / 2 - 30, 175));
                    break;
                case BodyParts.Right_Leg:
                    g.DrawLine(p, new Point(390 / 2, 130), new Point(390 / 2 + 30, 175));
                    break;
                case BodyParts.p:
                    if (isWin)
                    {
                        Pen pen = new Pen(Color.Blue, 5);
                        g.DrawLine(pen, new Point(390 / 2, 130), new Point(390 / 2 - 15, 105));
                        g.DrawEllipse(p, 390 / 2, 130, 10, 10);
                        g.DrawEllipse(p, 390 / 2 - 10, 130, 10, 10);
                    }
                    
                    break;
                default:
                    break;
            }
        }
        private void Draw(int wrongCount)
        {
            for (int i = 0; i < wrongCount; i++)
            {
                DrawBodyPart((BodyParts)i);
            }
        }
        private void Draw()
        {
            for (int i = 0; i < wrongCount; i++)
            {
                DrawBodyPart((BodyParts)i);
            }
        }
        private void CheckChar(char c)
        {
            if (word.Contains(c))
            {
                char[] letters = word.ToCharArray();
                for (int i = 0; i < letters.Length; i++)
                {
                    if (letters[i] == c)
                        labels[i].Text = c.ToString();//swap start to the entry char
                }
                foreach (Label l in labels)
                    if (l.Text == "*")
                    {
                       
                        return;
                    }

                isWin = true;
                panel1.Refresh();
                YouWin();

            }
            else
            {
                wrongCount++;
                labelWrong.Text = "Wrong " + wrongCount.ToString();
                Draw(wrongCount);
                ShowPictures();
                if (wrongCount == 9)
                {
                    YouLose();
                }
            }
        }
        private void YouLose()
        {
            sw.Stop();
            MessageBox.Show("You lose! \n Word: " + word, "Nice try");
            
            ResetGame();
        }
       
        private void YouWin()
        {
            isWin = true;        
            //  using (YouWin frm = new YouWin())
            //  {

            //  frm.ShowDialog();
            //  }            
            Draw(10);
            pictureBox.Image = imageList.Images[8];
            sw.Stop();
            MessageBox.Show("You win","CONGRATE");
           
            ResetGame();
        }
        private void ResetGame()
        {
            Graphics g = panel1.CreateGraphics();
            g.Clear(panel1.BackColor);
            wrongCount = 0;
            sw.Restart();
            GetRandomWord();
            MakeLabels();          
            DrawHangmanPost();
            Draw();
            LoadButtons();
            pictureBox.Image = null;//clear image
            isWin = false;
            for (int i = 0; i < buttons.Count; i++)
            {
                buttons[i].Enabled = true;
            }

        }
        private void ShowPictures()
        {
            if (wrongCount < 8)
                pictureBox.Image = imageList.Images[wrongCount];
        }

        #endregion

        private void Timer_Tick(object sender, EventArgs e)
        {
           
            labelTime.Text = "Timer: "+sw.Elapsed.Seconds ;
        }
    }
}
