import '../style/style.css';
function Car() {
	return (
		<div class="container">
			<form action="action_page.php" method="post">
				<div class="imgcontainer">
					<img src="img_avatar2.png" alt="Avatar" class="avatar"/>
				</div>

				<div class="container">
					<label for="uname"><b>Email</b></label>
					<input type="text" placeholder="Entrez votre email" name="uname" required/>

					<label for="psw"><b>Mot de passe</b></label>
					<input type="password" placeholder="Entrez votre mot de passe" name="psw" required/>

					<button type="submit">Login</button>
					<label>
					  <input type="checkbox" checked="checked" name="remember"/> Se souvenir
					</label>
				</div>

				<div class="container" style={{backgroundColor: '#f1f1f1'}}>
					<span class="psw">Mot de passe <a href="#"> oublié ? </a> </span>
				</div>
			</form> 

		</div>
	);
  
}

export default Car;