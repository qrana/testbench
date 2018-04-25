#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include <QProcess>
#include <QFileDialog>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    base = "";
    environment = "python";
    filename = "test_bench_output.csv";
    readFileName = "serial_reader.py";
    processFileName = "process_data.py";

    ui->setupUi(this);

    // Create connections between UI elements, signals and slots

    connect(ui->processButton, SIGNAL(clicked(bool)),
            this, SLOT(processData()));

    connect(ui->clearButton, SIGNAL(clicked(bool)),
            this, SLOT(clear()));

    connect(ui->getButton, SIGNAL(clicked(bool)),
            this, SLOT(read()));

    connect(ui->actionSelect_process_file, SIGNAL(triggered(bool)),
            this, SLOT(changeProcessFileName()));

    connect(ui->filenameLineEdit, SIGNAL(editingFinished()),
            this, SLOT(changeFileName()));

    connect(ui->actionSelect_read_file, SIGNAL(triggered(bool)),
            this, SLOT(changeReadFileName()));

//    connect(ui->sourceFileButton, SIGNAL(clicked(bool)),
//            this, SLOT(changeProcessFileName()));

    connect(ui->actionSelect_environment, SIGNAL(triggered(bool)),
            this, SLOT(changeEnvironment()));

    connect(ui->actionSelect_base, SIGNAL(triggered(bool)),
            this, SLOT(changeBase()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::clear()
{
    ui->outputTextEdit->setPlainText("");
}

void MainWindow::processData()
{
    QProcess OProcess;
    QString Command;  //Contains the command to be executed
    QStringList args;  //Contains arguments of the command

    // QString script(base + "/process_data.py");
    QString script = "process_data.py";

    Command = environment;
    args<<script;

    OProcess.setNativeArguments("\"" + filename + "\"");
    OProcess.start(Command,args); //Starts execution of command
    OProcess.waitForFinished(-1);  //Waits for execution to complete

    QString StdOut = OProcess.readAllStandardOutput();  //Reads standard output
    QString StdError = OProcess.readAllStandardError();   //Reads standard error

    QString output = "Standard output:\n"
                     + StdOut + "\n"
                     + "Standard error:\n"
                     + StdError + "\n";
    ui->outputTextEdit->setPlainText(output);
}

void MainWindow::read()
{
    QProcess OProcess;
    QString Command;  //Contains the command to be executed
    QStringList args;  //Contains arguments of the command

    // QString script(base + "/serial_reader.py");
    QString script = "serial_reader.py";

    Command = environment;
    args<<script;

    OProcess.setNativeArguments("\"" + filename + "\"");
    OProcess.start(Command,args); //Starts execution of command
    OProcess.waitForFinished(-1);  //Waits for execution to complete

    QString StdOut = OProcess.readAllStandardOutput();  //Reads standard output
    QString StdError = OProcess.readAllStandardError();   //Reads standard error

    QString output = "Standard output:\n"
                     + StdOut + "\n"
                     + "Standard error:\n"
                     + StdError + "\n";
    ui->outputTextEdit->setPlainText(output);
}

void MainWindow::changeFileName()
{
    filename = ui->filenameLineEdit->text();
}

void MainWindow::changeReadFileName()
{
    readFileName = QFileDialog::getOpenFileName(this,
                                                "Choose Filename to Run",
                                                "",
                                                ".csv files (*.csv);;All files (*.*)");
}

void MainWindow::changeProcessFileName()
{
    processFileName = QFileDialog::getOpenFileName(this,
                                            "Choose Filename to Run",
                                            "",
                                            ".csv files (*.csv);;All files (*.*)");
}

void MainWindow::changeEnvironment()
{
    environment = QFileDialog::getOpenFileName(this,
                                            "Choose Filename of interpreter",
                                            "",
                                            "All files (*.*)");
}

void MainWindow::changeBase()
{
    base = QFileDialog::getExistingDirectory(this, "Choose Filename to project base");
}
