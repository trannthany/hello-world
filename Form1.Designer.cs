namespace Hangman_V5
{
    partial class FormHangman
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(FormHangman));
            this.groupBoxTextInsertion = new System.Windows.Forms.GroupBox();
            this.buttonClose = new System.Windows.Forms.Button();
            this.textBoxWord = new System.Windows.Forms.TextBox();
            this.buttonSubmitWord = new System.Windows.Forms.Button();
            this.groupBoxButtons = new System.Windows.Forms.GroupBox();
            this.labelWrong = new System.Windows.Forms.Label();
            this.labelWordLength = new System.Windows.Forms.Label();
            this.groupBoxCanvas = new System.Windows.Forms.GroupBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.labelTime = new System.Windows.Forms.Label();
            this.pictureBox = new System.Windows.Forms.PictureBox();
            this.imageList = new System.Windows.Forms.ImageList(this.components);
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.groupBoxTextInsertion.SuspendLayout();
            this.groupBoxButtons.SuspendLayout();
            this.groupBoxCanvas.SuspendLayout();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBoxTextInsertion
            // 
            this.groupBoxTextInsertion.Controls.Add(this.buttonClose);
            this.groupBoxTextInsertion.Controls.Add(this.textBoxWord);
            this.groupBoxTextInsertion.Controls.Add(this.buttonSubmitWord);
            this.groupBoxTextInsertion.Location = new System.Drawing.Point(468, 274);
            this.groupBoxTextInsertion.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBoxTextInsertion.Name = "groupBoxTextInsertion";
            this.groupBoxTextInsertion.Padding = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBoxTextInsertion.Size = new System.Drawing.Size(450, 98);
            this.groupBoxTextInsertion.TabIndex = 6;
            this.groupBoxTextInsertion.TabStop = false;
            // 
            // buttonClose
            // 
            this.buttonClose.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.buttonClose.Location = new System.Drawing.Point(343, 68);
            this.buttonClose.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.buttonClose.Name = "buttonClose";
            this.buttonClose.Size = new System.Drawing.Size(86, 25);
            this.buttonClose.TabIndex = 2;
            this.buttonClose.Text = "Close";
            this.buttonClose.UseVisualStyleBackColor = true;
            this.buttonClose.Click += new System.EventHandler(this.ButtonClose_Click);
            // 
            // textBoxWord
            // 
            this.textBoxWord.Font = new System.Drawing.Font("Comic Sans MS", 15.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.textBoxWord.Location = new System.Drawing.Point(142, 22);
            this.textBoxWord.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.textBoxWord.Name = "textBoxWord";
            this.textBoxWord.Size = new System.Drawing.Size(287, 37);
            this.textBoxWord.TabIndex = 0;
            // 
            // buttonSubmitWord
            // 
            this.buttonSubmitWord.Location = new System.Drawing.Point(12, 22);
            this.buttonSubmitWord.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.buttonSubmitWord.Name = "buttonSubmitWord";
            this.buttonSubmitWord.Size = new System.Drawing.Size(124, 25);
            this.buttonSubmitWord.TabIndex = 2;
            this.buttonSubmitWord.Text = "Submit Word";
            this.buttonSubmitWord.UseVisualStyleBackColor = true;
            this.buttonSubmitWord.Click += new System.EventHandler(this.ButtonSubmitWord_Click);
            // 
            // groupBoxButtons
            // 
            this.groupBoxButtons.Controls.Add(this.labelWrong);
            this.groupBoxButtons.Controls.Add(this.labelWordLength);
            this.groupBoxButtons.Location = new System.Drawing.Point(470, 12);
            this.groupBoxButtons.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBoxButtons.Name = "groupBoxButtons";
            this.groupBoxButtons.Padding = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBoxButtons.Size = new System.Drawing.Size(455, 123);
            this.groupBoxButtons.TabIndex = 8;
            this.groupBoxButtons.TabStop = false;
            // 
            // labelWrong
            // 
            this.labelWrong.AutoSize = true;
            this.labelWrong.Location = new System.Drawing.Point(8, 18);
            this.labelWrong.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelWrong.Name = "labelWrong";
            this.labelWrong.Size = new System.Drawing.Size(45, 13);
            this.labelWrong.TabIndex = 1;
            this.labelWrong.Text = "Wrong: ";
            // 
            // labelWordLength
            // 
            this.labelWordLength.AutoSize = true;
            this.labelWordLength.Location = new System.Drawing.Point(338, 18);
            this.labelWordLength.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelWordLength.Name = "labelWordLength";
            this.labelWordLength.Size = new System.Drawing.Size(75, 13);
            this.labelWordLength.TabIndex = 0;
            this.labelWordLength.Text = "Word Length: ";
            // 
            // groupBoxCanvas
            // 
            this.groupBoxCanvas.Controls.Add(this.panel1);
            this.groupBoxCanvas.Location = new System.Drawing.Point(11, 12);
            this.groupBoxCanvas.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBoxCanvas.Name = "groupBoxCanvas";
            this.groupBoxCanvas.Padding = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBoxCanvas.Size = new System.Drawing.Size(455, 363);
            this.groupBoxCanvas.TabIndex = 9;
            this.groupBoxCanvas.TabStop = false;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.labelTime);
            this.panel1.Controls.Add(this.pictureBox);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(2, 16);
            this.panel1.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(451, 344);
            this.panel1.TabIndex = 5;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.Panel1_Paint);
            // 
            // labelTime
            // 
            this.labelTime.AutoSize = true;
            this.labelTime.Location = new System.Drawing.Point(286, 314);
            this.labelTime.Name = "labelTime";
            this.labelTime.Size = new System.Drawing.Size(36, 13);
            this.labelTime.TabIndex = 1;
            this.labelTime.Text = "Timer:";
            // 
            // pictureBox
            // 
            this.pictureBox.Location = new System.Drawing.Point(3, 3);
            this.pictureBox.Name = "pictureBox";
            this.pictureBox.Size = new System.Drawing.Size(128, 104);
            this.pictureBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox.TabIndex = 0;
            this.pictureBox.TabStop = false;
            // 
            // imageList
            // 
            this.imageList.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList.ImageStream")));
            this.imageList.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList.Images.SetKeyName(0, "1.png");
            this.imageList.Images.SetKeyName(1, "2.png");
            this.imageList.Images.SetKeyName(2, "3.png");
            this.imageList.Images.SetKeyName(3, "4.png");
            this.imageList.Images.SetKeyName(4, "5.png");
            this.imageList.Images.SetKeyName(5, "6.png");
            this.imageList.Images.SetKeyName(6, "7.png");
            this.imageList.Images.SetKeyName(7, "8.png");
            this.imageList.Images.SetKeyName(8, "YouWin.jpg");
            // 
            // timer
            // 
            this.timer.Tick += new System.EventHandler(this.Timer_Tick);
            // 
            // FormHangman
            // 
            this.AcceptButton = this.buttonSubmitWord;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.buttonClose;
            this.ClientSize = new System.Drawing.Size(927, 373);
            this.Controls.Add(this.groupBoxCanvas);
            this.Controls.Add(this.groupBoxTextInsertion);
            this.Controls.Add(this.groupBoxButtons);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.KeyPreview = true;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "FormHangman";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.Text = "Hangman_V5";
            this.Load += new System.EventHandler(this.FormHangman_Load);
            this.groupBoxTextInsertion.ResumeLayout(false);
            this.groupBoxTextInsertion.PerformLayout();
            this.groupBoxButtons.ResumeLayout(false);
            this.groupBoxButtons.PerformLayout();
            this.groupBoxCanvas.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.GroupBox groupBoxTextInsertion;
        private System.Windows.Forms.Button buttonClose;
        private System.Windows.Forms.TextBox textBoxWord;
        private System.Windows.Forms.Button buttonSubmitWord;
        private System.Windows.Forms.GroupBox groupBoxButtons;
        private System.Windows.Forms.Label labelWrong;
        private System.Windows.Forms.Label labelWordLength;
        private System.Windows.Forms.GroupBox groupBoxCanvas;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.PictureBox pictureBox;
        private System.Windows.Forms.ImageList imageList;
        private System.Windows.Forms.Timer timer;
        private System.Windows.Forms.Label labelTime;
    }
}

