<?php

use yii\db\Migration;

/**
 * Handles the creation of table `category`.
 */
class m170225_002743_create_category_table extends Migration
{
    public function safeUp(){
        $this->createTable('category', [
            'id' => $this->primaryKey(),
            'pid'=> $this->integer(),
            'name' => $this->string(200)->notNull(),
            'created_at' => $this->datetime(),
            'updated_at' => $this->datetime(),
            'sort'=> $this->integer()->defaultValue(0),
        ]);
        $this->addForeignKey('fk_category_pid', 'category', 'pid', 'category', 'id', 'CASCADE');
        $this->insert('category',['name'=>'PHP','sort'=>1]);
        $this->insert('category',['name'=>'DataBase','sort'=>3]);
        $this->insert('category',['name'=>'Linux', 'sort'=>5]);
    }
    /**
     * @inheritdoc
     */
    public function safeDown()
    {
        $this->dropForeignKey('fk_category_pid','category');
        $this->dropTable('category');
    }
}
