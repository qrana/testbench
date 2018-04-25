#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void clear();

    void processData();

    void read();

    void changeFileName();

    void changeReadFileName();

    void changeProcessFileName();

    void changeEnvironment();

    void changeBase();

private:
    Ui::MainWindow *ui;

    QString environment;
    QString base;

    QString filename;
    QString readFileName;
    QString processFileName;
};

#endif // MAINWINDOW_HH
