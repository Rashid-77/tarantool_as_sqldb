#!/usr/bin/env tarantool

function init()
    box.schema.space.create('dialog')
    box.execute(
        [[
            CREATE TABLE dialog 
            (
                id UNSIGNED PRIMARY KEY AUTOINCREMENT,
                user1_id UNSIGNED,
                user2_id UNSIGNED,
                msg STRING
            );
        ]])
end


box.cfg{listen = 3301}
box.once('init', init)


function insert_msg(u_id1, u_id2, msg)
    return box.execute(
        [[INSERT INTO dialog VALUES (NULL, ?, ?, ?);]], {u_id1, u_id2, msg}
    )
end


function select(id)
    return box.execute([[SELECT * FROM dialog WHERE id=(?);]], {id})
end


function select_all()
    return box.execute([[SELECT * FROM dialog;]])
end


function get_msg_from(u_id)
    return box.execute([[SELECT * FROM dialog WHERE user1_id=(?);]], {u_id})
end


function get_msg_to(u_id)
    return box.execute([[SELECT * FROM dialog WHERE user2_id=(?);]], {u_id})
end


function del_msg_id(id)
    return box.execute([[DELETE FROM dialog WHERE id=(?);]], {id})
end
