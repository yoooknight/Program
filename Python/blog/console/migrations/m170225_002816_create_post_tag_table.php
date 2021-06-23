<?php

use yii\db\Migration;

/**
 * Handles the creation of table `post_tag`.
 */
class m170225_002816_create_post_tag_table extends Migration
{
    /**
     * @inheritdoc
     */
    public function safeUp()
    {
        $this->createTable('post_tag', [
            'id' => $this->primaryKey(),
            'post_id' => $this->integer()->notNull(),
            'tag_id' => $this->integer()->notNull()]);

        $this->createIndex('post_tag_index', 'post_tag', ['post_id', 'tag_id']);
//	$this->addForeignKey('fk_post_tag_post', 'post_tag', 'post_id', 'post', 'id', 'CASCADE', 'CASCADE');
//	$this->addForeignKey('fk_post_tag_tag', 'post_tag', 'tag_id', 'tag', 'id', 'CASCADE', 'CASCADE');
    }

    /**
     * @inheritdoc
     */
    public function safeDown()
    {
//        $this->dropForeignKey('fk_post_tag_post', 'post_tag');
//        $this->dropForeignKey('fk_post_tag_tag', 'post_tag');
        $this->dropTable('post_tag');
    }
}
