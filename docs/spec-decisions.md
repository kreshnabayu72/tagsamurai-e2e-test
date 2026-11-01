# Keputusan atas Spec yang Tidak Terpenuhi

Dokumen ini mencatat setiap kali sebuah langkah spec meminta sesuatu yang **tidak terpenuhi** (oleh komponen, mock BE, atau konvensi), **karena apa**, dan **keputusannya**. Baca sebelum menulis atau memperbaiki skrip e2e. Langkah yang tercantum di sini dibangun sesuai keputusannya dan **bukan** kegagalan atau temuan baru.

Aturan:
- Satu entri per keputusan: `Spec / langkah`, `Spec meminta`, `Kenyataannya`, `Karena`, `Keputusan`, `Diterapkan di`.
- Entri ditambah saat pemilik spec memutuskan, dengan tanggal. Entri tidak dihapus; keputusan yang berubah menambah entri baru yang menyebut entri lama.
- Konvensi di `foundation` tidak diubah oleh entri di sini. Kalau konvensi dan keputusan berbeda, keputusan berlaku untuk spec e2e sampai konvensinya diperbarui.
- D-006 (spec draft Position) dan D-007 (spec Brand) hanya berlaku di branch evaluasi integrasi dan tidak ada di sini.
- Yang belum diputuskan tidak masuk sini: itu temuan (`plans/<slug>/integration-findings.md` di repo aplikasi).

## D-001 Panel filter hanya menutup lewat icon Filter (2026-10-25)

- **Spec / langkah:** `TC-AC-PP-E2E-034` langkah 35, `035` langkah 56, `036` langkah 10 (semula "klik di luar panel").
- **Spec meminta:** menutup panel Filter dengan klik di luar panel.
- **Kenyataannya:** FilterContainer bukan dialog; tidak ada tutup lewat klik luar. Panel menutup hanya lewat toggle icon Filter.
- **Karena:** perilaku asli produk. `prd-conventions` §9.8 masih menyebut klik luar panel; pemilik spec memutuskan itu diabaikan dulu.
- **Keputusan:** spec memakai "klik ulang icon Filter". Klik luar tidak diimplementasikan dan tidak diuji.
- **Diterapkan di:** spec 034, 035, 036 (commit `ab5962c8`).

## D-002 Perubahan yang belum di-Apply dibuang saat panel ditutup (2026-10-25)

- **Spec / langkah:** `TC-AC-PP-E2E-035` TC-AC-PP-116 (langkah 55 sampai 58).
- **Spec meminta:** menutup panel tanpa Apply membuang draft; field kembali ke nilai terakhir yang di-Apply.
- **Kenyataannya:** komponen mempertahankan draft yang belum di-Apply.
- **Karena:** kekurangan komponen, bukan kebijakan.
- **Keputusan:** spec benar; komponen yang diperbaiki.
- **Diterapkan di:** react-core `FilterContainer` (draft dibuang saat panel menutup tanpa Apply; story `DiscardOnClose`); spec 035 TC-116 mengasersi placeholder "All users" setelah dibuka lagi.

## D-003 Clear Field hanya mengosongkan draft (2026-10-25)

- **Spec / langkah:** semua langkah `[Clear Field]` di spec 034 sampai 037.
- **Spec meminta:** `[Clear Field]` mengosongkan field; filter di tabel baru berubah setelah `[Apply]`.
- **Kenyataannya:** komponen juga menerapkan filter kosong ke tabel saat `[Clear Field]` diklik.
- **Karena:** kekurangan komponen.
- **Keputusan:** `[Clear Field]` adalah bagian dari sistem draft: hanya mengosongkan nilai staged, tidak memicu Apply.
- **Diterapkan di:** react-core `FilterContainer` (story `ClearIsDraft`). Spec tidak berubah.

## D-004 Akurasi hasil Search diuji di e2e dengan API nyata (2026-10-25)

- **Spec / langkah:** `TC-AC-PP-E2E-033` TC-AC-PP-102 langkah 66, 67, 72.
- **Spec meminta:** kolom yang di-hide tidak ikut dicari, dan kembali dicari setelah di-unhide.
- **Kenyataannya:** mock BE di repo aplikasi tetap mencocokkan kolom tersembunyi.
- **Karena:** kolom mana yang dicari adalah hasil BE; repo aplikasi hanya me-mock BE.
- **Keputusan:** asersi akurasi dilewati di sini dan dikerjakan di e2e integrasi dengan API nyata. Langkah UI (hide, ketik, Enter, unhide) tetap jalan.
- **Diterapkan di:** spec 033 (catatan di Notes); skrip menandainya `// @real-api:`. `wangs-ui-agent-kit run-report` mendaftar semua tag `@real-api` sebagai pekerjaan suite real-API.

## D-005 Chip overflow mengikuti lebar field, jadi dua chip bisa tidak muat (2026-10-25)

- **Spec / langkah:** `TC-AC-PP-E2E-036` TC-AC-PP-201 langkah 5 sampai 9; `TC-AC-PP-E2E-034` TC-AC-PP-109 langkah 21.
- **Spec meminta:** chip tampil sebanyak yang muat pada lebar field, sisanya `+N more`, tanpa scroll horizontal (036); dan dua chip `John Doe` dan `Jane Smith` tampil (034).
- **Kenyataannya:** MultiSelect hanya punya `maxVisibleChips` berbasis jumlah, tanpa `+N more` yang mengikuti lebar. Setelah `maxVisibleChips="responsive"` ditambahkan, field filter selebar sekitar 213 px hanya memuat satu dari dua chip itu (82 px + sekitar 92 px + gap 8 px melebihi 181 px).
- **Karena:** aturan Overflow Chip (`prd-conventions` §9.8 butir 4) dan lebar field filter.
- **Keputusan:** komponen mengikuti aturan itu (`responsive`, dipakai FilterContainer). Spec 034 langkah 21 meminta `John Doe` dan `+1 more`; spec 036 tidak berubah.
- **Diterapkan di:** react-core `MultiSelect` dan `FilterContainer`; spec 034 langkah 21 (commit `68ddf89e`); skrip 034 dan 036.

## D-008 Setup Column berlaku setelah Save, bukan langsung (2026-10-26)

- **Spec / langkah:** `TC-AC-PP-E2E-044` TC-AC-PP-131 langkah 5, 11, 17.
- **Spec meminta:** kolom yang di-uncheck di popup Setup Column langsung hilang dari tabel di belakang popup, sebelum `[Save]`.
- **Kenyataannya:** tabel di belakang popup tidak berubah sampai `[Save]`; menutup popup tanpa Save membuang perubahan, sebagaimana `TC-AC-PP-E2E-043` TC-AC-PP-136 meminta.
- **Karena:** dua spec yang sama-sama dimiliki pemilik spec bertentangan (F-37); yang lain (043) sesuai perilaku Setup Column di PRD.
- **Keputusan:** 044 mengikuti 043 dan UI: langkah 5, 11, 17 meminta kolom masih tampil sampai Save. Live Preview di popup tetap terpisah (diuji bila `tableName` tersedia).
- **Diubah di:** spec 044 langkah 5, 11, 17 dan skrip.

## D-009 Copy dan zona waktu spec privacy-policy mengikuti TC doc dan General Settings (2026-10-26)

- **Spec / langkah:** `TC-AC-PP-E2E-004`, `022`, `024`, `028` (placeholder dan pesan V-01), `006` (tanggal Publish dan log), `022` (info bar).
- **Spec meminta:** `Enter Privacy Policy content` dan `Privacy Policy content must not be empty`; tanggal hari ini pada Time Zone General Settings (UTC); info bar tertulis `Version 3 · Published At 10 Aug 26 · Published By John D`; entri Activity Log dari Publish.
- **Kenyataannya:** TC doc (`tc-settings-privacy-policy.md`) menulis `Enter privacy policy content` (sejak 2026-10-13); tanggal ditampilkan di zona browser, bukan zona tenant; info bar terdiri dari elemen terpisah dan tanda `·` hanya notasi baca; entri Activity Log ditulis BE nyata, sedangkan mock log ada di browser dan tidak punya objek Privacy Policy.
- **Karena:** spec usang terhadap TC doc; aplikasi belum memakai Time Zone General Settings; PRD hanya menggambarkan susunan info bar; BE di-mock.
- **Keputusan:** copy di spec mengikuti TC doc (huruf kecil `privacy policy`); aplikasi memformat tanggal di Time Zone General Settings dan browser e2e berjalan di UTC; info bar diasersi per bagian; asersi entri Activity Log (006 langkah 17 dan 20 sampai 26) ditandai `@real-api`.
- **Perubahan app yang menyertai:** tanggal tabel dan formatter memakai `timezone` dari `generalSettings`; klik menu sidebar menghapus state query tabel (search, sort, filter, paginasi) dan me-remount halaman (prd-conventions, "re-klik menu tetap reset"); edit kebijakan yang kotor menahan Browser Back dan navigasi (menutup Publish Confirm atau menanyakan Unsaved Changes); seed tanggal memakai UTC.

## D-010 Set Password tanpa token dijawab 405, bukan 400 (2026-10-29)

- **Spec / langkah:** `TC-AUTH-ACT-E2E-020` TC-AUTH-ACT-132 langkah 21–22.
- **Spec meminta:** request Set Password tanpa token dijawab `400`.
- **Kenyataannya:** token adalah segmen path (`POST /v2/iam/auth/activation/{token}/set-password`). Request tanpa token menjadi `/activation//set-password`, dan router menjawab `405 Method Not Allowed`, status yang tercantum di kontrak operasi ini.
- **Karena:** kontrak tidak punya field body untuk dikosongkan; 405 berasal dari routing, sesuai kontrak.
- **Keputusan:** langkah 21–22 mengharapkan `405`. Backend tidak diubah.
- **Diterapkan di:** skrip 020.

## D-011 Request OTP dari dua tab hanya mengirim satu kode (2026-10-29)

- **Spec / langkah:** `TC-AUTH-OTP-E2E-046` TC-AUTH-OTP-173.
- **Spec meminta:** Request OTP untuk satu email dari dua tab menghasilkan dua mail OTP.
- **Kenyataannya:** request kedua jatuh dalam cooldown 60 detik dari request pertama (TC-AUTH-OTP-90), jadi server menolaknya dan hanya satu kode terkirim.
- **Karena:** cooldown memang mencegah kode ganda; dua tab tidak mengirim serentak.
- **Keputusan:** satu mail OTP; request kedua tertolak cooldown (UI menampilkan pesan cooldown) dan tidak ada mail kedua.
- **Diterapkan di:** skrip 046.

## D-012 Link reset dan konfirmasi email dari mail dibuka lewat route penerus di app (2026-10-29)

- **Spec / langkah:** spec `Auth/ResetPassword` yang membuka link reset dari mail; konfirmasi ganti email.
- **Spec meminta:** link di mail membuka halaman Setup New Password (dan halaman konfirmasi email).
- **Kenyataannya:** iam membangun `RESET_PASSWORD_URL` + `?token=` (default `/reset-password?token=`) dan `FRONTEND_BASE_URL` + `/confirm-email?token=`, sedangkan route app adalah `/auth/reset-password/setup/:token` dan belum ada route konfirmasi email.
- **Karena:** bentuk link backend dan route app tidak selaras (issue iam #103).
- **Keputusan:** app menambah route `/reset-password?token=` dan `/activate?token=` (link aktivasi dari template baru) yang meneruskan ke halaman yang ada; tanpa token, ke halaman Expired link alur itu. `/confirm-email?token=` menunggu halaman konfirmasi ganti email, yang belum ada di app. Backend tidak menunggu diubah; issue iam #103 tetap terbuka untuk penyelarasan.
- **Diterapkan di:** route app tagsamurai (commit `02795d1d`); skrip `TC-AUTH-ACT-E2E-023` TC-11 (mail berisi `/activate?token=`, link dibuka apa adanya lalu diteruskan ke Set Password).

## D-013 Kegagalan penulisan log tidak membatalkan aksi Auth (2026-10-29)

- **Spec / langkah:** `TC-AUTH-RST-E2E-037` TC-AUTH-RST-103 langkah 8–16; pola yang sama di `TC-AUTH-LP-153` (Login with Password, BT-33).
- **Spec meminta:** saat penulisan log dipaksa gagal, Request Reset dibatalkan: toast `Error, failed to send reset link.`, tidak ada mail, token tidak terbit (PRD reset-password §9.7: "Sync (atomik untuk token dan log)").
- **Kenyataannya:** iam menyimpan token di databasenya sendiri, sedangkan log ditulis ke service analytics yang terpisah dan di-retry bila gagal. Request Reset tetap sukses (`200`, layar Email Sent, mail terkirim), dan baris log masuk setelah service log pulih.
- **Karena:** token dan log berada di dua service, jadi tidak bisa atomik tanpa transaksi lintas service; aksi pengguna tidak boleh ikut gagal karena service log bermasalah. Spec tidak sepenuhnya memodelkan arsitektur backend.
- **Keputusan:** perilaku backend yang benar. Aksi tetap sukses, dan log menyusul lewat retry. Langkah TC-103 memverifikasi: Email Sent tampil, satu mail reset terkirim, dan baris log Reset Password muncul setelah injeksi dipulihkan.
- **Diterapkan di:** skrip 037 TC-103; berlaku juga untuk LP-153 (skrip LoginPassword dikerjakan tim lain).

## D-013a Password lebih dari 72 byte ditolak di browser, tanpa baris log (2026-10-29)

- **Spec / langkah:** `TC-AUTH-RST-E2E-027` TC-AUTH-RST-77 langkah 20–22 (dan TC-AUTH-RST-78 bila langkahnya sama).
- **Spec meminta:** password 73 karakter ditolak, lalu Session Log mencatat baris Failed "Password does not meet requirements".
- **Kenyataannya:** batas 72 byte diperiksa di browser sebelum request dikirim; backend tidak menerima apa pun, jadi tidak ada baris log.
- **Karena:** validasi di sisi aplikasi sudah cukup; penolakan yang tidak sampai ke server tidak menghasilkan log server.
- **Keputusan:** langkah log untuk penolakan di browser tidak berlaku. Skrip memverifikasi pesan penolakan di form dan bahwa tidak ada request reset yang terkirim.
- **Diterapkan di:** skrip 027.
- **Berlaku juga untuk:** `TC-AUTH-OTP-E2E-037` TC-AUTH-OTP-119 ("Empty OTP" pada Verify fallback): kode yang belum 6 digit ditolak di browser (PRD-TEXT-26), tidak ada request verify, jadi tidak ada baris log; skrip memverifikasi caption `OTP must not be empty` dan tidak ada request `otp/verify`.

## D-014 Tombol [Leave] pada dialog Unsaved Changes ber-severity primary (2026-10-29)

- **Spec / langkah:** `TC-GS-BRAND-E2E-014` dan `TC-GS-BRAND-E2E-019` (langkah verifikasi `[Leave]` "filled, warning"), serta setiap spec lain yang meminta `[Leave]` berwarna warning pada dialog Unsaved Changes form Create/Edit.
- **Spec meminta:** `[Leave]` filled, severity warning.
- **Kenyataannya:** dialog Unsaved Changes form Create/Edit memakai bentuk kanonis aplikasi: dialog warning, `[Leave]` primary, `[Cancel]` contrast.
- **Karena:** keputusan pemilik 2026-10-20 (bentuk kanonis seluruh aplikasi), ditegaskan 2026-10-28.
- **Keputusan:** `[Leave]` berwarna primary memenuhi langkah tersebut. Skrip memverifikasi severity `primary`.
- **Diterapkan di:** skrip 014 dan 019.

## D-015 URL langsung ke halaman tanpa capability diarahkan ke halaman no-access, tanpa toast (2026-10-29)

- **Spec / langkah:** `TC-GS-BRAND-E2E-010` TC-GS-BRAND-34 langkah 6–8, serta spec lain yang meminta toast "You don't have permission to do this." dan tidak ada redirect saat URL halaman yang tidak boleh dibuka diketik langsung.
- **Spec meminta:** toast error, UI di-refresh, tidak ada redirect.
- **Kenyataannya:** route guard aplikasi mengarahkan ke halaman no-access, tanpa toast. PRD Brand §2 dan aturan akses route tidak memakai toast untuk URL terlarang.
- **Karena:** perilaku route guard berlaku untuk seluruh aplikasi dan mengikuti PRD. Toast izin dipakai untuk aksi yang ditolak di halaman yang boleh dibuka, bukan untuk navigasi.
- **Keputusan:** langkah 6–8 dipenuhi oleh halaman no-access. Skrip memverifikasi halaman no-access tampil dan tidak ada baris Brand yang termuat (langkah 9).
- **Diterapkan di:** skrip 010.

## D-016 Emoji di field teks dibuang di level input, tanpa pesan error (2026-10-29)

- **Spec / langkah:** `TC-GS-BRAND-E2E-068` TC-GS-BRAND-230 (emoji di Brand Name memunculkan "Brand Name contains invalid characters"), dan spec lain yang meminta pesan error untuk emoji yang diketik.
- **Spec meminta:** pesan error validasi untuk emoji.
- **Kenyataannya:** field teks membuang emoji saat diketik, saat blur, dan saat submit, sehingga validator dan server tidak pernah menerimanya.
- **Karena:** konvensi PRD §4 dan TC-048 menetapkan emoji diblokir di level input. Spec yang meminta pesan error bertentangan dengan keduanya.
- **Keputusan:** langkah dipenuhi bila emoji tidak masuk ke field dan nama yang tersimpan tidak mengandung emoji. Skrip memverifikasi isi field setelah mengetik emoji, bukan pesan error.
- **Diterapkan di:** skrip 068.

## D-017 Password kosong ditolak di browser sebelum cek lock (2026-10-29)

- **Spec / langkah:** `TC-AUTH-LP-E2E-010` TC-AUTH-LP-42 ([Log in] dengan Password kosong saat akun terkunci 15 menit menampilkan Alert lock).
- **Spec meminta:** lock dievaluasi lebih dulu daripada Password kosong.
- **Kenyataannya:** browser menolak Password kosong sebelum request apa pun; hanya server yang tahu status lock.
- **Karena:** memenuhi urutan spec butuh perubahan di frontend dan backend (iam memeriksa lock sebelum validasi `required`). Backend mengikuti kontraknya, dan perubahan backend hanya atas perintah pemilik.
- **Keputusan:** langkah dipenuhi oleh pesan "Password must not be empty" tanpa request login. Alert lock diverifikasi pada percobaan dengan Password terisi.
- **Diterapkan di:** skrip 010.

## D-018 Setelah 409 karena versi kebijakan berubah, user kembali ke Login (2026-10-29)

- **Spec / langkah:** `TC-AUTH-LP-E2E-026` TC-AUTH-LP-87 (setelah Privacy Policy berubah, Confirm to Continue dimuat ulang dan Continue berhasil).
- **Spec meminta:** Confirm dimuat ulang dengan versi baru, lalu Continue berhasil.
- **Kenyataannya:** kontrak backend (openapi, Bruno, unit test) memakai habis token pra-autentikasi pada `409` dan mengembalikan user ke Login (BT-47).
- **Karena:** backend mengikuti kontraknya; perubahan backend hanya atas perintah pemilik.
- **Keputusan:** setelah `409`, aplikasi kembali ke halaman Login; user login ulang lalu menyetujui versi baru. Aplikasi disesuaikan, dan skrip memverifikasi alur itu.
- **Diterapkan di:** aplikasi (alur 409 di Confirm to Continue) dan skrip 026.

## D-019 Timeout pada write memakai pesan "Connection problem. Please try again." (2026-10-29)

- **Spec / langkah:** `TC-GS-BRAND-E2E-070` TC-GS-BRAND-67 langkah 25 (Create yang timeout menampilkan "Error, failed to create brand."), dan spec lain yang meminta pesan 5xx untuk kegagalan timeout atau jaringan.
- **Spec meminta:** toast "Error, failed to create brand." saat request Create timeout.
- **Kenyataannya:** konvensi error-handling (foundation `error-handling-convention.md` §2 "Timeout / Network") memakai toast "Connection problem. Please try again." tanpa tombol aksi. Form tetap terbuka, input dipertahankan, dan tombol kembali aktif untuk retry manual. PRD Brand §9.6 meminta form tetap terbuka dengan input dipertahankan. PRD tidak menetapkan durasi timeout.
- **Karena:** konvensi lintas modul untuk kegagalan jaringan lebih spesifik daripada teks 5xx milik modul.
- **Keputusan:** timeout dan kegagalan jaringan pada write menampilkan "Connection problem. Please try again." dan membiarkan form terbuka untuk retry. "Error, failed to create brand." tetap untuk 5xx. Durasi timeout klien ditetapkan 30 detik, mulai dari write Brand (create, rename, delete).
- **Diterapkan di:** aplikasi (write Brand) dan skrip 070.

## D-020 Button di Choose Verification Method bertuliskan [Next] (2026-10-30)

- **Spec / langkah:** suite `Auth/Mfa`: setiap langkah yang menyebut Button [Login] di Halaman Choose Verification Method (antara lain `TC-AUTH-MFA-E2E-001` TC-AUTH-MFA-01 dan TC-AUTH-MFA-02, `TC-AUTH-MFA-E2E-040` langkah 10 dan 27).
- **Spec meminta:** Button [Login] di Halaman Choose Verification Method.
- **Kenyataannya:** wireframe PRD MFA S-AUTHMFA-01 menulis "Login", tetapi product owner menetapkan CTA halaman pemilihan metode adalah "Next". Halaman OTP Verification dan Authenticator Verification tetap memakai "Login".
- **Karena:** keputusan product owner atas teks CTA. Di halaman ini user baru memilih metode dan belum masuk.
- **Keputusan:** Button di Halaman Choose Verification Method adalah [Next]. Semua aturan lain pada spec tetap berlaku untuk Button tersebut, misalnya disabled sampai metode dipilih.
- **Diterapkan di:** skrip suite Auth/Mfa.

## D-021 Geo-IP tidak tersedia diuji di backend, tidak di e2e (2026-10-30)

- **Spec / langkah:** `TC-AUTH-OTP-E2E-050` TC-AUTH-OTP-192, seluruh langkah (geo-IP service dimatikan, lalu login dari lokasi lebih dari 100 km melewati trigger MFA lokasi).
- **Spec meminta:** environment e2e dapat mematikan dan menyalakan geo-IP service (failure injection), lalu memverifikasi login OTP lanjut ke Portal tanpa MFA, tanpa error, dan tanpa email alert login tak biasa.
- **Kenyataannya:** backend tidak punya route untuk membuat lookup geo-IP gagal. Override lokasi (`/dev/geo`) hanya mengganti hasil lookup. TC sumber menandai TC-AUTH-OTP-192 sebagai Manual Only.
- **Karena:** aturan fail-open (lookup geo-IP gagal berarti trigger jarak dan negara dilewati) adalah logika backend yang lebih tepat dijaga oleh unit test backend. Route fault khusus untuk satu spec tidak sepadan.
- **Keputusan:** spec 050 tidak diotomasi (`coverage.web: manual`). Perilaku fail-open dijaga oleh unit test backend, yang dilacak di iam #112. Issue itu tetap terbuka sampai unit test-nya ada di `dev`.
- **Diterapkan di:** spec 050 (status coverage) dan skrip 050 (tidak dijalankan).

## D-022 Lock yang melewati tengah malam: bagian aktif dijaga unit test backend (2026-10-30)

- **Spec / langkah:** `TC-AUTH-LP-E2E-013` TC-AUTH-LP-55 langkah 31–36 (lock 15 menit sejak 23:55 masih menolak login pada 00:05 hari berikutnya).
- **Spec meminta:** membekukan jam server uji pada 00:05 hari berikutnya, lalu memverifikasi Alert lock 15 menit tetap tampil.
- **Kenyataannya:** backend tidak punya route untuk memajukan atau membekukan jam server. `ageTime` menggeser waktu kegagalan dan akhir lock bersamaan, sehingga lock yang dimulai kemarin tidak bisa tetap aktif saat ini.
- **Karena:** perilaku ini sudah dijaga unit test backend `TestLogin_TimedLockCrossesMidnight` (`iam-service` `internal/modules/auth/service/login_service_test.go`).
- **Keputusan:** langkah 31–36 tidak diotomasi di e2e dan dijaga unit test tersebut. Langkah 37–42 (setelah lock berakhir, hitungan hari baru mulai dari 1) tetap diotomasi dengan `ageTime`. Issue iam #113 ditutup.
- **Diterapkan di:** skrip 013 (TC-AUTH-LP-55).

## D-023 Kode MFA terkirim otomatis pada digit ke-6 (2026-10-30)

- **Spec / langkah:** suite `Auth/Mfa`: langkah yang mengisi 6 digit kode (OTP email atau Authenticator) lalu mengklik [Login] atau [Verify] (antara lain spec 010, 011, 012, 029, 030, 034, 035, 037, 039, 041, 044, 046, 049, 056).
- **Spec meminta:** user mengklik [Login] atau [Verify] setelah kode 6 digit lengkap.
- **Kenyataannya:** aplikasi mengirim kode begitu digit ke-6 terisi, sama seperti Login with OTP (PRD F-AUTHOTP-05 dan FI-01). Setelah itu layar sudah berpindah atau tombol sedang sibuk, sehingga klik manual tidak bisa dilakukan.
- **Karena:** auto-submit pada digit terakhir adalah perilaku umum isian kode OTP, dan diputuskan owner.
- **Keputusan:** pada layar verifikasi MFA, kode terkirim otomatis pada digit ke-6. Langkah "klik [Login]/[Verify]" setelah kode lengkap dipenuhi oleh pengiriman otomatis itu, dan hasil langkah berikutnya tetap diverifikasi. Klik tombol hanya diuji pada isian yang belum lengkap, misalnya untuk memastikan tombol disabled atau memunculkan caption.
- **Diterapkan di:** skrip suite Auth/Mfa.

## D-024 Batas tepat 24 jam link aktivasi dijaga unit test backend (2026-10-30)

- **Spec / langkah:** `TC-AUTH-ACT-E2E-027` TC-AUTH-ACT-137 langkah 10–13 (link berusia tepat 24 jam 00 menit 00 detik masih menampilkan Set Password).
- **Spec meminta:** jam server uji di-set tepat 24 jam 00 menit 00 detik setelah token terbit, lalu link dibuka.
- **Kenyataannya:** e2e hanya bisa menggeser umur token (`ageTime`), sementara jam server terus berjalan. Detik tepat itu tidak bisa dicapai.
- **Karena:** batas inklusif adalah logika backend (`time.Now().After(token.ExpiresAt)`), yang lebih tepat dijaga oleh unit test dengan clock yang bisa disuntikkan. Route pembeku jam untuk satu batas ini tidak sepadan.
- **Keputusan:** TC-AUTH-ACT-137 tidak diotomasi di e2e. Batasnya dijaga unit test backend yang dilacak di iam #115, dan issue itu tetap terbuka sampai test-nya ada di `dev`. TC-AUTH-ACT-87, TC-AUTH-ACT-124 dan TC-AUTH-ACT-86 tetap diotomasi dengan `ageTime`.
- **Diterapkan di:** skrip 027 (TC-AUTH-ACT-137).

## D-025 Token reset email lama yang lolos invalidasi dijaga unit test backend (2026-10-30)

- **Spec / langkah:** `TC-AUTH-RST-E2E-023` TC-AUTH-RST-141 langkah 20–26 (token milik email lama yang belum di-invalidate callback ditolak 404 dan dicatat "Reset link expired").
- **Spec meminta:** kondisi email user sudah berganti sementara token reset email lama masih aktif.
- **Kenyataannya:** alur ganti email yang normal selalu menjalankan callback yang meng-invalidate token, jadi kondisi itu tidak bisa dibuat tanpa route khusus test.
- **Karena:** pemeriksaan cadangan ini (`validate_reset_password_service.go`, kecocokan email token dengan email user) sudah dijaga unit test backend `TestValidate_UnusableOwnerKillsTheToken`, kasus "email changed".
- **Keputusan:** TC-AUTH-RST-141 tidak diotomasi di e2e. TC-AUTH-RST-114 dan TC-AUTH-RST-133 tetap diotomasi. Issue iam #116 ditutup.
- **Diterapkan di:** skrip 023 (TC-AUTH-RST-141).

## D-026 Rollback Submit New Password dijaga integration test backend (2026-10-30)

- **Spec / langkah:** `TC-AUTH-RST-E2E-037` TC-AUTH-RST-92 langkah 26–33 (kegagalan setelah password disimpan dan sebelum commit tidak meninggalkan perubahan sebagian).
- **Spec meminta:** injeksi kegagalan di tengah transaksi Submit, lalu memverifikasi password lama masih berlaku dan lock permanen belum dibuka.
- **Kenyataannya:** backend tidak punya route fault untuk transaksi Submit. Seluruh langkah reset sudah berjalan dalam satu transaksi (`confirm_reset_password_service.go`). Unit test yang ada memakai repository tiruan, sehingga belum membuktikan rollback di database.
- **Karena:** rollback adalah perilaku transaksi database yang lebih tepat dibuktikan oleh integration test backend dengan Postgres asli daripada route fault khusus e2e.
- **Keputusan:** TC-AUTH-RST-92 tidak diotomasi di e2e. Rollback dijaga integration test backend yang dilacak di iam #117, dan issue itu tetap terbuka sampai test-nya ada di `dev`. TC-AUTH-RST-21, TC-AUTH-RST-103 dan TC-AUTH-RST-144 tetap diotomasi.
- **Diterapkan di:** skrip 037 (TC-AUTH-RST-92).

## D-027 Baris tab Session Activity Log disiapkan dengan seed, bukan aksi nyata (2026-10-30)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-017` sampai `TC-GS-ACTLOG-E2E-023`, bagian Prerequisites (tabel data awal, kolom "Cara").
- **Spec meminta:** baris tab Session dibentuk lewat aksi nyata: login dengan password benar dan salah, logout manual, membuka card Global Settings, meminta Reset Password, dan Change Password di My Profile.
- **Kenyataannya:** langkah yang diuji ketujuh spec ini adalah search, filter, dan sort pada tab Session. Aksi nyata hanya menyiapkan baris, tetapi menghasilkan waktu dan urutan yang tidak bisa diatur, bergantung pada modul lain (Change Password belum punya endpoint), dan terkena rate limit, pemicu MFA, serta reCAPTCHA.
- **Karena:** halaman Activity Log diuji pada perilakunya sendiri. Ketepatan baris yang ditulis oleh aksi nyata diuji di suite alurnya masing-masing (LoginPassword, ResetPassword, SessionManagement) lewat API log.
- **Keputusan:** baris tab Session pada ketujuh spec ini disiapkan dengan seed lewat route dev `session-logs`. Nilai Activity, Status, Note, dan kolom snapshot diambil dari nilai yang memang ditulis backend (kontrak dan asersi spec alurnya), bukan dikarang. Semua langkah bernomor tetap diotomasi.
- **Diterapkan di:** skrip ActivityLog 017, 018, 019, 020, 021, 022, 023.

## D-028 Pindah halaman saat popup form terisi dipicu Back browser, bukan menu sidebar (2026-10-30)

- **Spec / langkah:** `TC-GS-POS-E2E-013` TC-GS-POS-64 langkah 51 dan 57, `TC-GS-POS-E2E-018` TC-GS-POS-103 langkah 59 (klik menu sidebar Global Settings > General Settings saat popup Create/Edit Position terisi).
- **Spec meminta:** klik menu sidebar selagi popup terbuka, lalu dialog Unsaved Changes mencegat perpindahan halaman.
- **Kenyataannya:** popup form menutup layar dengan scrim, sehingga sidebar tidak bisa diklik, dan popup tidak tertutup oleh klik di luarnya. Pengguna tidak pernah bisa memilih menu sidebar selagi popup terbuka.
- **Karena:** yang diuji TC ini adalah guard perpindahan halaman di dalam app saat form terisi. Selagi popup terbuka, perpindahan itu hanya bisa terjadi lewat Back/Forward browser, dan guard yang sama yang mencegatnya.
- **Keputusan:** klik menu sidebar diganti Back (action `navigateBack`: Back browser di web, Back sistem di Android). Guard hanya mencegat Back bila halaman sebelumnya dibuka di dalam app, jadi sebelum popup dibuka skrip berpindah ke tab User List lalu kembali ke tab Position. Setelah `[Leave]`, yang diverifikasi adalah halaman sebelumnya itu (tab User List aktif), bukan General Settings. Langkah verifikasi dialog, `[Cancel]`, dan `[Leave]` tetap diotomasi.
- **Diterapkan di:** skrip Position 013 (TC-GS-POS-64) dan 018 (TC-GS-POS-103).

## D-029 Name beremoji yang "lolos validasi klien" diuji lewat request langsung (2026-10-31)

- **Spec / langkah:** `TC-GS-DIV-E2E-073` TC-GS-DIV-270 langkah 31-44 (Edit) dan TC-GS-DIV-267 langkah 45-57 (Create): injeksi `Finance 😀` langsung ke DOM field Division Name, klik [Save]/[Submit], lalu penolakan server tampil di form.
- **Spec meminta:** nilai beremoji melewati validasi klien lewat DOM, lalu form menampilkan penolakan server.
- **Kenyataannya:** form menghapus emoji saat input, saat blur, dan sekali lagi saat submit (D-016). Nilai beremoji tidak pernah sampai ke request, jadi form tidak mungkin menampilkan penolakan server.
- **Karena:** yang diuji TC ini adalah pertahanan server terhadap nilai yang tidak lolos validasi klien. Request langsung menguji hal yang sama, seperti TC-GS-DIV-259 sampai 262 di spec yang sama.
- **Keputusan:** Create dan Edit dengan Name `Finance 😀` dikirim langsung ke server dengan sesi aktor. Yang diverifikasi: server menolak dengan validasi pada Name, Division tidak dibuat, dan Name tidak berubah (dicek di tabel). Langkah yang hanya ada di form (modal tetap terbuka, input dipertahankan, penolakan tampil di form, ✕, dan Unsaved Changes) tidak diotomasi, karena keadaan itu tidak bisa terjadi.
- **Diterapkan di:** skrip Division 073 (TC-GS-DIV-270, TC-GS-DIV-267).

## D-030 Layar Auth mengikuti layout AuthShell, bukan Card terpusat (2026-10-31)

- **Spec / langkah:** `TC-AUTH-OTP-E2E-001` TC-AUTH-OTP-01 langkah 3; `TC-AUTH-MFA-E2E-001` TC-AUTH-MFA-01 langkah 8; `TC-AUTH-MFA-E2E-004` TC-AUTH-MFA-04 langkah 10; `TC-AUTH-MFA-E2E-009` TC-AUTH-MFA-05 langkah 9; `TC-AUTH-MFA-E2E-014` TC-AUTH-MFA-07 langkah 10 dan 13.
- **Spec meminta:** form tampil dalam Card `Elevated` terpusat di canvas penuh; tiga langkah Enrollment tampil dalam satu card.
- **Kenyataannya:** semua layar Auth memakai AuthShell, yaitu dua kolom: panel brand di kiri dan form di kanan, tanpa Card.
- **Karena:** keputusan owner. Spec UI tidak akurat, dan UI aplikasi sudah berkembang lebih baik daripada spec.
- **Keputusan:** layout AuthShell dipertahankan. Langkah yang memverifikasi Card terpusat atau satu card tidak diotomasi. Isi layar (judul, subjudul, field, dan tombol) tetap diverifikasi.
- **Diterapkan di:** skrip Login OTP 001 dan MFA 001, 004, 009, 014.

## D-031 Tautan Privacy Policy terpisah dari label checkbox, mengikuti PRD (2026-10-31)

- **Spec / langkah:** `TC-AUTH-OTP-E2E-002` TC-AUTH-OTP-09 langkah 33 (teks "Privacy Policy" pada label checkbox berupa tautan ke halaman Privacy Policy).
- **Spec meminta:** kata "Privacy Policy" di label checkbox Agreement bisa diklik.
- **Kenyataannya:** label checkbox polos "I have read and agree to the Privacy Policy *". Dokumen dibuka lewat tautan terpisah "Read the full Privacy Policy" di bawah teks persetujuan.
- **Karena:** PRD login-password §4.2b menetapkan susunan itu: teks persetujuan dengan tautan "Read the full Privacy Policy", lalu checkbox berlabel polos. Satu tautan ke dokumen sudah cukup, dan label checkbox tetap berfungsi mencentang.
- **Keputusan:** mengikuti PRD. Langkah 33 diverifikasi pada tautan "Read the full Privacy Policy", bukan pada label checkbox.
- **Diterapkan di:** skrip Login OTP 002 (TC-AUTH-OTP-09).

## D-032 Tautan [Reset password] tampil inline di dalam Alert (2026-10-31)

- **Spec / langkah:** `TC-AUTH-LP-E2E-012` TC-AUTH-LP-50 langkah 17 dan TC-AUTH-LP-51 langkah 26; `TC-AUTH-LP-E2E-013` TC-AUTH-LP-56 langkah 48; `TC-AUTH-LP-E2E-014` TC-AUTH-LP-58 langkah 6 dan TC-AUTH-LP-59 langkah 12.
- **Spec meminta:** tautan [Reset password] tampil satu baris di bawah teks Alert (PRD login-password §4.3, FI-AUTHLP-10).
- **Kenyataannya:** tautan tampil inline tepat setelah kalimat Alert, dipisah satu spasi, dan ikut membungkus bersama teks.
- **Karena:** keputusan product owner pada 2026-10-20, ditegaskan lagi oleh owner pada 2026-10-31 karena tampilannya lebih rapi.
- **Keputusan:** tautan inline di dalam Alert. Langkah-langkah itu memverifikasi tautan [Reset password] ada di dalam Alert dan membuka Reset Password, bukan posisinya satu baris di bawah teks.
- **Diterapkan di:** skrip Login Password 012, 013, 014.

## D-033 Chip TC-GS-ACTLOG-82 memakai nama literal di entitas log-terbatas (2026-10-31)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-021` TC-GS-ACTLOG-82 langkah 17-21 (Data uji TC-GS-ACTLOG-82, Client A: `John Doe {runId}-021`/`Budi Anwar {runId}-021`, `Staff {runId}-021`/`Supervisor {runId}-021`, `Marketing {runId}-021`/`Finance {runId}-021`, `Login`/`Logout`, `Success`/`Failed`).
- **Spec meminta:** dua opsi dicentang di tiap field, lalu kedua chip tampil di dalam field yang tertutup.
- **Kenyataannya:** pada jendela 1280px, panel filter memuat empat field per baris. Satu chip `John Doe {runId}-021` saja sudah memenuhi field, dan pasangan nama literal `John Doe` + `Budi Anwar` pun meleset beberapa piksel. Chip kedua masuk ke `+1 more`, sehingga kedua chip tidak pernah tampil bersama.
- **Karena:** keputusan owner: nama dipendekkan dan jendela diperlebar. Nama tanpa sufiks hanya unik di entitas segar milik spec ini, yaitu `entitasLog021`, yang sudah memuat `John Doe`, `Budi Anwar`, `Staff`, `Supervisor`, `Marketing`, `Finance`, `Login`, dan `Logout` dengan nama literal TC.
- **Keputusan:** TC-GS-ACTLOG-82 berjalan pada jendela 1440px. Pasangan User, Position, Division, dan Activity diuji di `entitasLog021` dengan nama literal TC. Pasangan Status (`Success`/`Failed`) tetap di Client A, karena nilainya tanpa sufiks dan `entitasLog021` hanya memuat `Success` (TC-GS-ACTLOG-78).
- **Diterapkan di:** skrip Activity Log 021 (TC-GS-ACTLOG-82).

## D-034 Ukuran file tampil maksimal dua desimal, nol di ujung dibuang (2026-10-31)

- **Spec / langkah:** `TC-GS-FILEMGR-E2E-002` TC-GS-FILEMGR-05 langkah 16-21 dan TC-GS-FILEMGR-06 (kolom Size), serta spec lain yang membaca sel Size.
- **Spec meminta:** satu desimal, pembulatan half-up (PRD file-manager §4.2a baris Size), misalnya `1.3 MB` untuk 1.310.720 byte.
- **Kenyataannya:** backend memformat ukuran dengan dua desimal (`1.00 KB`, `1.25 MB`).
- **Karena:** keputusan owner. Ukuran diformat backend dengan maksimal dua desimal; bila desimal kedua nol, ditampilkan satu desimal (`1.00` jadi `1.0`, `2.40` jadi `2.4`), sedangkan dua desimal yang bermakna tetap (`1.25`).
- **Keputusan:** sel Size diverifikasi dengan aturan itu: `1.0 KB`, `512.0 KB`, `1.0 MB`, `1.25 MB`, `2.4 MB`, `1.5 GB`. Satuan tetap naik setelah pembulatan sesuai PRD (1.048.575 byte tampil `1.0 MB`). Backend masih perlu membuang nol di ujung (BT-89).
- **Diterapkan di:** skrip File Manager 002 dan fixture `fileManager.json`.

## D-035 Dialog Duplicate Login Attempt dan tombol Confirm-nya berseverity danger (2026-10-31)

- **Spec / langkah:** `TC-AUTH-SES-E2E-001` TC-AUTH-SES-1 langkah 3-7 dan 10-12; `TC-AUTH-SES-E2E-007` TC-AUTH-SES-17 langkah 6-9.
- **Spec meminta:** dialog dan tombol [Confirm] berseverity warning (PRD session-management S-05).
- **Kenyataannya:** dialog dan [Confirm] berseverity danger; [Cancel] tetap contrast.
- **Karena:** override product owner yang sudah tertulis di aplikasi (`useDuplicateLoginAttempt.ts`): mengonfirmasi berarti mengakhiri sesi di device lain, jadi aksinya destruktif. Keputusan UI menang atas PRD.
- **Keputusan:** langkah-langkah itu memverifikasi severity danger untuk dialog dan [Confirm].
- **Diterapkan di:** skrip Session Management 001 dan 007.

## D-036 Kotak kode MFA satu baris enam kotak, bukan dua grup tiga (2026-10-31)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-004` TC-AUTH-MFA-04 langkah 15; `TC-AUTH-MFA-E2E-009` TC-AUTH-MFA-05 langkah 13.
- **Spec meminta:** SegmentedInput 6 kotak digit dalam dua grup tiga kotak.
- **Kenyataannya:** enam kotak dalam satu baris selebar tombol.
- **Karena:** PRD mfa §4 hanya menyebut "SegmentedInput 6 digit" tanpa pengelompokan; lebar kotak sama dengan tombol adalah keputusan owner 2026-10-19. Keputusan UI menang.
- **Keputusan:** langkah itu memverifikasi enam kotak dalam satu grup.
- **Diterapkan di:** skrip MFA 004 dan 009.

## D-037 reCAPTCHA yang belum diverifikasi ditolak browser sebelum lock diperiksa (2026-10-31)

- **Spec / langkah:** `TC-AUTH-LP-E2E-010` TC-AUTH-LP-43 langkah 10-11.
- **Spec meminta:** submit tanpa reCAPTCHA selama lock 15 menit aktif menampilkan Alert lock, dan reCAPTCHA tanpa caption error (lock diperiksa sebelum reCAPTCHA).
- **Kenyataannya:** browser menolak reCAPTCHA yang belum diverifikasi saat [Log in] diklik. Caption "Please verify that you are not a robot" tampil di bawah widget dan tidak ada request login, sehingga lock di server tidak ditanya.
- **Karena:** PRD login-password V-AUTHLP-05 memvalidasi reCAPTCHA "saat klik Log in" dengan caption di bawah widget, sama seperti field wajib lain (pola D-017). Urutan "lock sebelum captcha" pada catatan ordering PRD berlaku untuk request yang sampai ke server.
- **Keputusan:** langkah 10-11 memverifikasi caption reCAPTCHA, nol request login, dan tidak ada Alert. Alert lock diverifikasi pada langkah 5 (request dengan reCAPTCHA terverifikasi).
- **Diterapkan di:** skrip Login Password 010.

## D-038 Tanpa role "Manage user and role" tidak ada menu User sama sekali (2026-10-31)

- **Spec / langkah:** `TC-GS-DIV-E2E-007` TC-GS-DIV-18 langkah 68-71; `TC-GS-POS-E2E-007` TC-GS-POS-25 langkah 1-4.
- **Spec meminta:** halaman Global Settings > User terbuka, Tab `User List` tampil, dan Tab Division/Position Hidden.
- **Kenyataannya:** aktor tanpa role apa pun tidak mendapat menu User. Global Settings menampilkan halaman "You don't have access to any menu yet.", tanpa tab.
- **Karena:** PRD role §2.1 (role.md:293, :339): role "Manage user and role" men-gate menu User dan Role & Permission; "User tanpa role Manage user and role: tidak ada akses ke menu ini sama sekali".
- **Keputusan:** langkah-langkah itu memverifikasi halaman tanpa menu dan tidak ada tab maupun elemen tabel; elemen Hidden lainnya tetap diverifikasi.
- **Diterapkan di:** skrip Division 007 dan Position 007.

## D-039 Urutan bawaan tabel tidak menampilkan panah sort (2026-10-31)

- **Spec / langkah:** `TC-GS-DIV-E2E-001` TC-GS-DIV-3 langkah 24; `TC-GS-DIV-E2E-053` TC-GS-DIV-190 langkah 15; spec lain yang meminta ikon sort kolom default menunjukkan arah pada keadaan awal.
- **Spec meminta:** ikon sort kolom default (Name pada tabel Division, Date pada Changelog) menunjukkan arah urutan bawaan sebelum ada klik.
- **Kenyataannya:** urutan bawaan berasal dari API dan semua kolom netral (tanpa panah) sampai diklik.
- **Karena:** prd-conventions §9.7: pada State Awal tabel menampilkan urutan bawaan dan kolom tanpa sort aktif netral; klik ketiga "menghilangkan indikator panah sort aktif" dan mengembalikan urutan bawaan. Keputusan owner 2026-10-31: urutan default adalah urutan API, tanpa opsi tambahan di tabel.
- **Keputusan:** langkah itu memverifikasi urutan baris bawaan dan ikon sort netral.
- **Diterapkan di:** skrip Division 001 dan 053.

## D-040 Login baru menggantikan login lain yang masih menunggu Confirm Duplicate Login (2026-10-31)

- **Spec / langkah:** `TC-AUTH-SES-E2E-012` TC-AUTH-SES-321 langkah 49-57.
- **Spec meminta:** dua dialog Duplicate Login (Browser B dan C) tetap valid; Confirm B mengakhiri sesi A, lalu Confirm C mengakhiri sesi B.
- **Kenyataannya:** login C meng-invalidate login B yang masih menunggu (iam: satu handoff aktif per user, client, dan platform, sama seperti MFA EC-34). Confirm B ditolak 422; Confirm C berhasil dan mengakhiri sesi A.
- **Karena:** PRD session-management tidak mengatur dua dialog bersamaan (skenario hanya ada di dokumen TC). Satu login tertunda per user adalah aturan backend yang konsisten, dan PRD EC-21 sudah mengatur token pra-autentikasi yang tidak berlaku lagi: ditolak 422, FE kembali ke Login dengan toast `Error, failed to log in.`.
- **Keputusan:** langkah-langkah itu memverifikasi Confirm B kembali ke Login dengan toast dan sesi A tetap aktif; Confirm C masuk Portal dan mengakhiri sesi A; Browser B tanpa sesi; Browser A tidak menerima dialog Duplicate Login.
- **Diterapkan di:** skrip Session Management 012.

## D-041 Verifikasi bahasa ditunda sampai fitur final (2026-10-31)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-008` TC-GS-ACTLOG-27 (ganti bahasa, kolom verbatim vs translatable), serta langkah lain di spec mana pun yang mengganti bahasa lewat Language picker atau memverifikasi teks terjemahan non-Inggris.
- **Spec meminta:** ganti bahasa ke non-Inggris lalu verifikasi kolom/teks yang ikut diterjemahkan dan yang tetap verbatim.
- **Kenyataannya:** terjemahan app belum final; copy dan kunci terjemahan masih berubah per fitur.
- **Karena:** keputusan owner 2026-10-31: soal bahasa dikerjakan serentak setelah fitur final.
- **Keputusan:** langkah-langkah bahasa tidak dijalankan di e2e untuk sementara; TC yang seluruhnya tentang bahasa ditandai `// @spec-decision: D-041 TC-…`, langkah bahasa di TC lain ditandai `// @ui-gap: D-041 TC-… steps …`. Langkah lain di spec yang sama tetap dijalankan. Ditinjau ulang saat fitur final.
- **Diterapkan di:** skrip Activity Log 008 dan spec lain yang punya langkah bahasa.

## D-042 Aktor bernama satu kata tidak mungkin ada (2026-10-31)

- **Spec / langkah:** `TC-GS-POS-E2E-038` TC-GS-POS-292 langkah 39, 42-43; spec lain yang memakai aktor atau user bernama satu kata (mis. `Budi`, `Bagas`).
- **Spec meminta:** Modified By aktor bernama satu kata tampil `Budi` dan tooltip-nya `Budi`.
- **Kenyataannya:** user tidak dapat dibuat tanpa Last Name; iam menolak dengan 422 "Last name must not be empty".
- **Karena:** PRD user V-02: Last Name wajib.
- **Keputusan:** langkah untuk aktor bernama satu kata tidak dijalankan (`// @ui-gap: D-042 …`); langkah nama depan panjang di TC yang sama tetap dijalankan.
- **Diterapkan di:** skrip Position 038; CustomFieldUser 018 TC-450 memakai alasan yang sama.

## D-043 Klik backdrop tidak menutup Dialog Duplicate Login Attempt (2026-11-01)

- **Spec / langkah:** `TC-AUTH-SES-E2E-011` TC-AUTH-SES-31 langkah 23-28; `TC-AUTH-SES-E2E-066` TC-AUTH-SES-31 (bagian absence) langkah 24-28.
- **Spec meminta:** klik area gelap di luar dialog menutup Dialog Duplicate Login Attempt dengan efek Cancel.
- **Kenyataannya:** dialog tetap terbuka. Dialog ini confirm Modal Wangs UI (`useModals().confirm`), yang tidak bisa ditutup lewat klik backdrop; Escape tetap menutupnya karena dialog ini memakai opsi `closeOnEscape` (TC-AUTH-SES-30).
- **Karena:** perilaku komponen. Modal adalah overlay blocking yang hanya ditutup lewat aksi eksplisit (`Modal.spec.md`: "cannot be dismissed by clicking the overlay").
- **Keputusan:** perilaku komponen berlaku. Langkah backdrop memverifikasi dialog tetap terbuka dan tidak ada perubahan sesi; dialog lalu ditutup lewat [Cancel]. Bagian absence (tidak ada entri log) tetap diverifikasi.
- **Diterapkan di:** skrip SessionManagement 011 dan 066.

## D-044 Input kosong ditolak di client, tanpa request dan tanpa baris Failed (2026-11-01)

- **Spec / langkah:** `TC-AUTH-LP-E2E-035` TC-AUTH-LP-105 langkah 4, TC-AUTH-LP-106 langkah 13; `TC-AUTH-MFA-E2E-033` TC-AUTH-MFA-158 langkah 10-15, TC-AUTH-MFA-162 langkah 40-45; `TC-AUTH-MFA-E2E-028` TC-AUTH-MFA-133 langkah 90-91.
- **Spec meminta:** [Log in] dengan Password kosong, reCAPTCHA belum diselesaikan, atau kode kosong dikirim ke server; server mencatat baris Failed (`Empty password`, `Captcha not completed`, `Empty OTP`) dan menghitung percobaan kosong.
- **Kenyataannya:** form menolak di client (field Required, kode kurang dari 6 digit) dan menampilkan caption-nya sendiri; tidak ada request, jadi tidak ada baris log dan percobaan kosong tidak dihitung.
- **Karena:** keputusan owner (Zain Kurnia) 2026-11-01: validasi di client sudah benar. PRD F-AUTHLP-02 langkah 5-6 dan §9.8 tidak diikuti untuk input kosong dari UI.
- **Keputusan:** langkah-langkah itu memverifikasi caption client dan tidak adanya request. Pemeriksaan server untuk request kosong yang dikirim langsung (bukan dari UI) tetap dijalankan bila skripnya sudah ada (LP 035).
- **Diterapkan di:** skrip LoginPassword 035, Mfa 033 dan 028.

## D-045 Paste selalu mengisi dari kotak 1 (2026-11-01)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-004` TC-AUTH-MFA-88 langkah 92-97; `TC-AUTH-OTP-E2E-012` TC-AUTH-OTP-46 langkah 22-28.
- **Spec meminta:** paste `123456` setelah klik kotak 3 mengisi kotak 3-6 dengan 1-4, kotak 1-2 kosong, tanpa verifikasi otomatis.
- **Kenyataannya:** paste mulai dari kotak 1, mengisi keenam kotak, dan digit ke-6 langsung memverifikasi kode.
- **Karena:** keputusan owner (Zain Kurnia) 2026-11-01: perilaku komponen benar, spec yang salah. `SegmentedInput` Wangs UI menyimpan kode sebagai satu string berurutan (`Snap-to-End Clamping`, `SegmentedInput.spec.md`).
- **Keputusan:** langkah paste dari kotak 3 tidak dijalankan (`// @spec-decision: D-045 …`), karena akan memverifikasi kode yang salah. Perilaku paste diuji di komponen Wangs UI.
- **Diterapkan di:** skrip Mfa 004 dan LoginOtp 012.

## D-046 Back setelah sesi pre-auth berakhir kembali ke Login (2026-11-01)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-028` TC-AUTH-MFA-129 langkah 22-24, TC-AUTH-MFA-130 langkah 49-51; `TC-AUTH-MFA-E2E-031` TC-AUTH-MFA-150 langkah 108.
- **Spec meminta:** Back ke halaman kode setelah sesi pre-auth berakhir, lalu mengetik kode di sana.
- **Kenyataannya:** halaman kode sudah diganti di history; Back mendarat di Choose Verification Method, yang menolak token pre-auth yang tidak berlaku lagi dan menggantinya dengan Login. Tidak ada kotak kode untuk diketik.
- **Karena:** keputusan owner (Zain Kurnia) 2026-11-01: perilaku app dibiarkan; token pre-auth yang sudah berakhir tidak boleh melanjutkan login.
- **Keputusan:** kode tidak diketik ulang setelah Back. Mfa 028 memverifikasi Back berakhir di Login tanpa sesi; Mfa 031 (login sudah berhasil) memverifikasi tetap tepat satu baris Success (langkah 110-111).
- **Diterapkan di:** skrip Mfa 028 dan 031.

## D-047 Setelah Backspace, kotak aktif adalah kotak kosong berikutnya (2026-11-01)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-004` TC-AUTH-MFA-67 langkah 51 dan 54; `TC-AUTH-MFA-E2E-009` TC-AUTH-MFA-101 langkah 79 dan 82; `TC-AUTH-MFA-E2E-014` TC-AUTH-MFA-121 langkah 71 dan 74.
- **Spec meminta:** setelah Backspace, fokus kembali ke kotak terakhir yang terisi (kotak 2, lalu kotak 1).
- **Kenyataannya:** kotak aktif adalah tempat digit berikutnya masuk: kotak 3 setelah `12`, kotak 2 setelah `1`.
- **Karena:** keputusan owner (Zain Kurnia) 2026-11-01: perilaku `SegmentedInput` Wangs UI sudah benar.
- **Keputusan:** langkah-langkah itu memverifikasi kotak 3, lalu kotak 2 (`shouldHaveActiveSlotIndex(2)`, lalu `(1)`).
- **Diterapkan di:** skrip Mfa 004, 009 dan 014.

## D-048 Urutan Tab di Set up authenticator app: [Verify] lalu [Cancel] (2026-11-01)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-014` TC-AUTH-MFA-16 langkah 40.
- **Spec meminta:** setelah kotak digit, fokus berpindah ke [Cancel], lalu [Verify].
- **Kenyataannya:** [Verify] (button utama, lebar penuh) tampil di atas [Cancel] (button teks) dalam satu kolom, sehingga urutan Tab adalah [Verify], lalu [Cancel].
- **Karena:** keputusan owner (Zain Kurnia) 2026-11-01: perilaku app sudah benar. Urutan Tab mengikuti urutan tampilan.
- **Keputusan:** langkah 40 memverifikasi fokus pada [Verify], lalu [Cancel].
- **Diterapkan di:** skrip Mfa 014.
