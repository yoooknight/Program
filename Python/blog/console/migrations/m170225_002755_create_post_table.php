<?php

use yii\db\Migration;

/**
 * Handles the creation of table `post`.
 */
class m170225_002755_create_post_table extends Migration
{
    public function up()
    {
        $this->createTable('post', [
            'id' => $this->primaryKey(),
            'title' => $this->string(128)->notNull(),
            'lead_photo' => $this->string(500),
            'lead_text' => $this->text(),
            'content' => $this->text()->notNull(),
            'created_at' => $this->datetime(),
            'updated_at' => $this->datetime(),
            'category_id' => $this->integer()->notNull(),
            'view_count'=> $this->integer()->defaultValue(1),
            'on_top'=> $this->integer()->defaultValue(0),
            'comments_count'=> $this->integer()->defaultValue(0),
            'status'=> $this->integer()->defaultValue(0),
            'sort'=> $this->integer()->defaultValue(0),
        ]);

//        $this->addForeignKey('fk_post_category', 'post', 'category_id', 'category', 'id', 'CASCADE');
    }

    public function down()
    {
//        $this->dropForeignKey('fk_post_category', 'post');
        $this->dropTable('post');
    }
}
