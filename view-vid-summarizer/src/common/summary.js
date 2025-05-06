import './summary.css';

function Summary(props) {
    return (
       <>
       <br />
       <br />
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',flexDirection:'column'}}>
            <div className='summary-header'>
                Summary
            </div>
            <div class="summary-textbox-class">
                {props.summarizedText}
            </div>
        </div>
        </>
    );
}

export default Summary;