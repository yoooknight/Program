<?php

use yii\db\Migration;

/**
 * Handles the creation of table `tag`.
 */
class m170225_002804_create_tag_table extends Migration
{
    /**
     * @inheritdoc
     */
    public function safeup()
    {
        $this->createTable('tag', [
            'id' => $this->primaryKey(),
            'name' => $this->string(200)->notNull(),
            'created_at' => $this->datetime(),
            'updated_at' => $this->datetime(),
            'sort'=> $this->integer()->defaultValue(0),
        ]);

        $this->insert('tag',['name'=>'YII2','sort'=>1]);
        $this->insert('tag',['name'=>'MySql','sort'=>2]);
        $this->insert('tag',['name'=>'Linux','sort'=>3]);
        $this->insert('tag',['name'=>'Nginx','sort'=>4]);
        $this->insert('tag',['name'=>'API','sort'=>7]);
        $this->insert('tag',['name'=>'REST','sort'=>8]);
    }


    /**
     * @inheritdoc
     */
    public function safeDown()
    {
        $this->dropTable('tag');
    }
}
