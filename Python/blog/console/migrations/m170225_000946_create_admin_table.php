<?php

use yii\db\Migration;

/**
 * Handles the creation of table `admin`.
 */
class m170225_000946_create_admin_table extends Migration
{
    public function safeUp()
    {
        $this->createTable('admin', [
            'id' => $this->primaryKey(),
            'username' => $this->string()->notNull()->unique(),
            'auth_key' => $this->string(32)->notNull(),
            'password_hash' => $this->string()->notNull(),
            'password_reset_token' => $this->string()->unique(),
            'email' => $this->string()->unique(),
            'wechat_id' => $this->string(100),
            'status' => $this->smallInteger()->defaultValue(10),
            'created_at' => $this->integer(),
            'updated_at' => $this->integer(),
        ]);
        // create admin user:admin,password:123456
        $this->insert('admin',
            [
                'username'=>'admin',
                'password_hash'=>'e10adc3949ba59abbe56e057f20f883e',
                'email'=>'ws12138@163.com',
                'wechat_id'=>'8888',
                'status'=>10
            ]);
    }
    /**
     * @inheritdoc
     */
    public function safeDown()
    {
        $this->dropTable('admin');
    }


    public function actions()
    {
        return [
            'error' => [
                'class' => 'yii\web\ErrorAction',
            ],
            'captcha' => [
                'class' => 'yii\captcha\CaptchaAction',
                'maxLength'=>4,
                'minLength'=>4,
            ],
        ];
    }


    public function behaviors()
    {
        return [
            'access' => [
                'class' => AccessControl::className(),
                'rules' => [
                    [
                        'actions' => ['login', 'error', 'captcha',],
                        'allow' => true,
                    ],
                    [
                        'actions' => ['logout', 'index'],
                        'allow' => true,
                        'roles' => ['@'],
                    ],
                ],
            ],
            'verbs' => [
                'class' => VerbFilter::className(),
                'actions' => [
                    'logout' => ['post'],
                ],
            ],
        ];
    }
}
