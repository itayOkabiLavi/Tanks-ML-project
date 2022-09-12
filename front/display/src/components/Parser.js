import Tank from "./Tank"

export default function Parser() {
    const JSON_SEP = ','
    const TURN_SEP = ';'
    const SETUP_TO_GAME_SEP = 'G'
    const NEW_BULLET = 'new_bullet'

    function _parseSprites (JSON_Array, start_row) {
        let objects = []
        let i = start_row
        while (JSON_Array[i].trim() !== 'g') {
            let tank_det = JSON_Array[i].trim()
            tank_det = JSON.parse(tank_det)
            let tank = new Tank(tank_det)
            objects.push(tank)
            i += 1
        }
        i += 1   // skip  separator
        return [objects, i]
    }

    function _new_bullet(turn_list) {
        return {
            _id: NEW_BULLET,
            details: {
                id: turn_list[1].trim(),
                xpos: turn_list[2].trim(),
                ypos: turn_list[3].trim(),
                size: turn_list[4].trim(),
                color_rot: turn_list[5].trim()    
            }
        }
    }

    function _updating_turn(turn_list) {
        return {
            _id: turn_list[0].trim(),
            xpos: turn_list[1].trim(),
            ypos: turn_list[2].trim(),
            rot: turn_list[3].trim(),
            tur_rot: turn_list[4].trim()
        }
    }
    function _parseFrames (frame_array, i) {
        let frames = []
        while (typeof frame_array[i] === 'string') {
            let frame = {};
            frame_array[i].trim().split(TURN_SEP).forEach(turn => {

                turn = turn.trim().slice(1,-1); // remove spaces before & after string + chars '[',']'
                if (turn !== "") {
                    let turn_list = turn.split(JSON_SEP);
                    
                    if (turn_list[0].trim() == "b") turn = _new_bullet(turn_list)
                    else turn = _updating_turn(turn_list)
                    
                    frame[turn._id] = turn;
                }
            });
            frames.push(frame);
            i += 1;
        }
        return [frames, i]
    }

    this.parseGameFile = (game_text) => {
        const info_split = game_text.split('\n');
        let gameID = info_split[0].trim()
        let i = 1;
        let objects = []
        let sprites = []
        let frames = []
        
        [objects, i] = _parseSprites(info_split, i)
        console.log(objects)

        objects.forEach(object => sprites.push(object.render()))
        console.log(sprites)

        [frames, i] = _parseFrames(info_split, i)
        console.log(frames)

        return [gameID, objects, sprites, frames]
    }
}