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
- **Diterapkan di:** react-core `MultiSelect` dan `FilterContainer`; spec 034 langkah 21 (commit `68ddf89e`); skrip 034 dan 036; skrip Division 058 (`TC-GS-DIV-E2E-058` TC-GS-DIV-233 langkah 5-7: chip pertama + `+N more`, tanpa scroll horizontal, 2026-11-02).

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
- **Diterapkan di:** skrip 068; skrip Division 024 (langkah 5-7: nama tanpa emoji valid, isi field diverifikasi, tanpa Save; 2026-11-02).

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
- **Diterapkan di:** skrip Division 073 (TC-GS-DIV-270, TC-GS-DIV-267); skrip Custom Field User 013 (TC-GS-UCF-468 langkah 43-52: rename opsi Dropdown beremoji, form menolaknya inline, 2026-11-02).

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

## D-049 Respons yang ditahan untuk mengamati loading: 2 detik, bukan 5 (2026-11-01)

- **Spec / langkah:** `TC-AUTH-ACT-E2E-018` TC-AUTH-ACT-02 langkah 1 dan 3; `TC-AUTH-ACT-E2E-028` TC-AUTH-ACT-64 langkah 37 dan 39; `TC-AUTH-OTP-E2E-010` TC-AUTH-OTP-29 langkah 14, 16 dan 19; `TC-AUTH-OTP-E2E-013` TC-AUTH-OTP-42 langkah 18, 21 dan 24.
- **Spec meminta:** respons ditahan 5 detik, lalu halaman diamati selama 5 detik dan respons diteruskan normal.
- **Kenyataannya:** request auth di client punya timeout 5 detik (keputusan owner 2026-11-01, ui-items #24). Penahanan 5 detik, ditambah waktu jawab server, sampai ke client setelah timeout, sehingga yang tampil toast gagal (misalnya "Error, failed to send the code."), bukan alur sukses yang diminta spec.
- **Karena:** keputusan koordinator (didelegasikan owner) 2026-11-01. Tujuan langkahnya adalah mengamati loading selama request berjalan dan alur sukses setelahnya; durasi yang tidak sampai timeout tetap memenuhi tujuan itu. Kasus timeout sendiri diuji terpisah (TC-AUTH-MFA-157, penahanan 20 detik).
- **Keputusan:** respons ditahan 2 detik (`// @spec-decision: D-049 …`).
- **Diterapkan di:** skrip AccountActivation 018 dan 028, LoginOtp 010 dan 013.

## D-050 Toast sesi MFA berakhir tampil di halaman Login (2026-11-01)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-029` TC-AUTH-MFA-125 langkah 15.
- **Spec meminta:** setelah dialihkan ke Login karena sesi pre-auth habis, tidak ada toast.
- **Kenyataannya:** halaman Login menampilkan toast "Your MFA session has expired. Please log in again." satu kali setelah pengalihan itu.
- **Karena:** keputusan product owner (tagsamurai `plans/auth/decisions.md`, 2026-10-20): toast ditambahkan di atas PRD mfa V-11. Keputusan UI mengalahkan PRD (aturan owner 2026-10-31); dicatat koordinator (didelegasikan owner) 2026-11-01.
- **Keputusan:** langkah 15 memverifikasi toast itu tampil (`// @spec-decision: D-050 …`).
- **Diterapkan di:** skrip Mfa 029.

## D-051 Chip yang meluap di field filter Changelog/Activity Log: chip pertama + `+N more` (2026-11-02)

- **Spec / langkah:** `TC-GS-POS-E2E-040` TC-GS-POS-214 langkah 38-40; `TC-GS-ACTLOG-E2E-031` TC-GS-ACTLOG-171 langkah 5.
- **Spec meminta:** dua opsi dicentang, lalu kedua chip tampil di field yang tertutup (`Delete` dan `Create`; `Division` dan `Brand Name`).
- **Kenyataannya:** field filter Changelog (sekitar 173 px) dan field Field di Activity Log pada jendela 1280px hanya memuat satu chip. Chip kedua masuk ke `+1 more`.
- **Karena:** aturan Overflow Chip (`prd-conventions` §9.8 butir 4) dan D-005. Memperlebar jendela (D-033) hanya menguji lebar jendela, bukan aturan overflow; D-033 tetap khusus untuk nama literal di TC-GS-ACTLOG-82. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah memverifikasi chip pertama dan `+1 more`, serta kedua opsi tercentang di daftar opsi.
- **Diterapkan di:** skrip Position 040, Activity Log 031, Custom Field User 063 (TC-GS-UCF-266 langkah 23-29).

## D-052 Opsi Modified By di filter Changelog berlabel nama lengkap (2026-11-02)

- **Spec / langkah:** `TC-GS-UCF-E2E-063` TC-GS-UCF-264 langkah 12-13, 16-17, dan setiap langkah berikutnya yang memilih opsi atau membaca chip Modified By.
- **Spec meminta:** opsi filter Modified By di Changelog berlabel nama pendek (`Budi S`).
- **Kenyataannya:** opsi berlabel nama lengkap (`Budi Santoso`), sesuai facet dari server.
- **Karena:** PRD custom-field-user l.293 menetapkan `[First Name] [Last Initial]` hanya untuk kolom Changelog, tanpa aturan label opsi (aturan label opsi pendek l.264 milik tabel utama); kontrak analytics-reporting (`activity-log/API/openapi.yaml:1100-1103`) mengirim `modifiedByOptions` sebagai nama lengkap. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah memverifikasi opsi dan chip bernama lengkap (`Budi Santoso`, `Siti Rahmawati`, `Sari Dewi`); sel tabel tetap nama pendek.
- **Diterapkan di:** skrip Custom Field User 063.

## D-053 Urutan baris dengan Data Type sama tidak ditetapkan (2026-11-02)

- **Spec / langkah:** `TC-GS-UCF-E2E-054` TC-GS-UCF-222 langkah 13 dan 16.
- **Spec meminta:** sort Data Type, lalu baris dengan Data Type sama berurut Field Name A-Z.
- **Kenyataannya:** server mengurutkan dua baris Date sebagai Joining Date, lalu Birth Date.
- **Karena:** PRD custom-field-user §4.1.1 (baris Data Type, l.260) hanya menetapkan `Alphabetical (A-Z)`; `prd-conventions` §9.7 menetapkan tiebreaker hanya untuk kolom `+N more`. Tidak ada aturan urutan kedua. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah memverifikasi pengelompokan menurut Data Type (urutan A-Z / Z-A antar kelompok), bukan urutan di dalam kelompok.
- **Diterapkan di:** skrip Custom Field User 054, termasuk sort Required (TC-GS-UCF-224 langkah 31, 34, 37: baris dengan nilai Required sama).

## D-054 Nilai kosong di Changelog tampil `—` (2026-11-02)

- **Spec / langkah:** `TC-GS-UCF-E2E-061` TC-GS-UCF-253 langkah 15-17.
- **Spec meminta:** Old Value / New Value kosong tampil `-`.
- **Kenyataannya:** komponen Changelog bersama menampilkan `—` untuk semua modul.
- **Karena:** PRD file-manager l.276, non-login-user l.310/344, hardware-ble-gateway l.333 dan activity-log menetapkan `—`; hanya custom-field-user l.291 yang menulis `-`. Satu komponen Changelog dipakai semua modul, jadi tampilannya mengikuti mayoritas PRD. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah memverifikasi `—`.
- **Diterapkan di:** skrip Custom Field User 061.

## D-055 Nomor halaman di luar jangkauan dibawa ke halaman terakhir (2026-11-02)

- **Spec / langkah:** `TC-GS-UCF-E2E-055` langkah 19-20; `TC-GS-FILEMGR-E2E-036` (langkah input halaman `99`).
- **Spec meminta:** mengetik `99` di input halaman lalu Enter membuat tabel tetap di halaman 1.
- **Kenyataannya:** input halaman Paginator Wangs UI dibatasi ke jumlah halaman, sehingga `99` membawa tabel ke halaman terakhir, tanpa error.
- **Karena:** `prd-conventions` §9.11 hanya menetapkan "input nomor halaman → Enter → ke halaman tersebut", tanpa aturan untuk nomor di luar jangkauan. Membawa ke halaman terakhir adalah pola umum (quick jumper) dan tidak pernah menampilkan halaman kosong. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah memverifikasi tabel di halaman terakhir dan tidak ada error; `abc` tetap di halaman yang sama.
- **Diterapkan di:** skrip Custom Field User 055, File Manager 036.

## D-056 Daftar bullet di dialog konfirmasi baru bisa di-scroll di atas batas tampil (2026-11-02)

- **Spec / langkah:** `TC-GS-UCF-E2E-041` TC-GS-UCF-165 langkah 67, serta langkah yang sama di TC-GS-UCF-166 dan follow-up dengan sedikit nama.
- **Spec meminta:** daftar nama field terpilih berada dalam container scrollable, juga untuk tiga nama.
- **Kenyataannya:** daftar dibungkus area scroll hanya bila jumlahnya melebihi batas tampil (5); tiga nama tampil utuh tanpa container scroll.
- **Karena:** `prd-conventions` l.733 menetapkan daftar entitas "scrollable, jumlah tampil dibatasi, tidak diringkas"; scroll baru bermakna bila daftar melebihi batas tampil. PRD custom-field-user BA-01a/BA-02a tidak menetapkan ambang lain. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** dengan nama lebih dari 5, langkah memverifikasi container scrollable; dengan 5 nama atau kurang, langkah memverifikasi semua nama tampil utuh.
- **Diterapkan di:** skrip Custom Field User 041.

## D-057 Keyboard mencapai `⋯` (Column Visibility) lewat baris header grid (2026-11-02)

- **Spec / langkah:** `TC-GS-POS-E2E-001` langkah 52 ("Tab hingga fokus pada ⋯"); langkah serupa di tabel lain.
- **Spec meminta:** menekan Tab berulang sampai fokus berada di tombol `⋯` di header tabel.
- **Kenyataannya:** tabel adalah grid dengan satu tab stop. Tab masuk ke sel body pertama, ArrowUp pindah ke baris header, lalu Tab mencapai tombol `⋯`. Tab saja melompati header.
- **Karena:** pola grid (WAI-ARIA Grid) memakai satu tab stop dan navigasi panah di dalamnya; PRD tidak menetapkan urutan Tab di dalam tabel. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah mencapai `⋯` dengan Tab ke grid, ArrowUp ke baris header, lalu Tab; Enter membuka menu.
- **Diterapkan di:** skrip Position 001; react-core DataTable (tombol `⋯` dapat difokus, wangs-ui `f12585e9a`).

## D-058 User Pending Activation dengan kode OTP aktif dibuat lewat hapus lalu buat ulang (2026-11-02)

- **Spec / langkah:** `TC-AUTH-OTP-E2E-019` TC-AUTH-OTP-184 langkah 3 (dan Prerequisites "fixture BE yang dapat mengembalikan status user ke Pending Activation").
- **Spec meminta:** status user `Rudi Hartono` dikembalikan ke Pending Activation lewat fixture BE setelah kode OTP terbit, tanpa meng-invalidasi kode.
- **Kenyataannya:** tidak ada aksi admin atau API yang mengembalikan user Activated ke Pending Activation (AUTHACT-LOGIC-02c, transisi satu arah); fixture itu menulis state yang tidak pernah dihasilkan produk. Akun Pending dengan kode OTP yang sudah terbit tetap bisa terjadi: admin menghapus user (soft delete membebaskan email) lalu membuat user baru dengan email yang sama. Kode OTP berkunci email dan tidak di-invalidasi oleh penghapusan, dan Verify OTP memeriksa status akun sebelum kode, sehingga hasilnya sama dengan EC-49.
- **Karena:** state disusun seperti terjadinya di produk. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah 3 dijalankan sebagai admin (Global Settings > User): hapus `Rudi Hartono`, lalu buat user baru `Rudi Hartono` dengan email yang sama (Pending Activation, tidak diaktivasi). Baseline langkah 4 dan asersi langkah 12 memakai user baru tersebut. Langkah 5-12 tidak berubah.
- **Diterapkan di:** skrip Login OTP 019 (TC-AUTH-OTP-184).

## D-059 Token aktivasi tetap Active setelah pengiriman gagal dijaga unit test backend (2026-11-02)

- **Spec / langkah:** `TC-AUTH-ACT-E2E-024` TC-AUTH-ACT-17 langkah 7 (bagian "token aktivasi tetap Active").
- **Spec meminta:** memverifikasi status user Pending Activation dan token aktivasi tetap Active.
- **Kenyataannya:** status token tidak punya permukaan UI maupun API produk (PRD account-activation §9.7: disimpan di Auth); token mentah hanya ada di email yang gagal terkirim. Yang teramati user dan admin adalah badge Pending Activation di Global Settings > User > Login User.
- **Karena:** nilai internal yang tidak dapat diamati; dijaga unit test backend pada cabang kegagalan pengiriman Activation Email (token tidak diubah), issue iam menyusul. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah 7 memverifikasi badge Pending Activation user `Intan Ramadhan` di tabel Login User setelah 15 menit. "Akun masih bisa diaktivasi" dibuktikan oleh Resend pada TC-AUTH-ACT-18 (langkah 9-14).
- **Diterapkan di:** skrip Account Activation 024 (TC-AUTH-ACT-17).

## D-060 Data lock 052 diverifikasi lewat caption lock; hitungan hari berturut-turut dijaga unit test backend (2026-11-02)

- **Spec / langkah:** `TC-AUTH-LP-E2E-052` TC-AUTH-LP-163 langkah 42-44.
- **Spec meminta:** membaca data lock user lewat fixture BE (langkah 42), memverifikasi hitungan hari berturut-turut tetap 1 (langkah 43), dan status akun bukan Requires Reset dan bukan Permanent (langkah 44).
- **Kenyataannya:** status akun sudah terlihat oleh user sebagai caption lock: langkah 41 menampilkan lock 15 menit, bukan lock 1 jam, Requires Reset, atau Permanent. Hitungan hari berturut-turut adalah penghitung internal tanpa permukaan UI atau API produk (login-password.md l.789). Bukti publiknya (eskalasi Permanent pada hari ke-8, seperti spec 014) butuh enam hari lock 1 jam lagi dan tidak masuk alur satu hari TC-AUTH-LP-163.
- **Karena:** nilai internal yang tidak dapat diamati; dijaga unit test backend (reset data lock harian tidak mengubah hitungan hari berturut-turut, AUTHLP-LOGIC-02l), issue iam menyusul. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah 44 diverifikasi pada caption langkah 41 (tidak ada Alert Requires Reset maupun Permanent). Langkah 42-43 tidak diotomasi di e2e dan dijaga unit test backend tersebut.
- **Diterapkan di:** skrip Login Password 052 (TC-AUTH-LP-163).

## D-061 Password tersimpan berspasi tidak ada di V2; "password tidak di-trim" dibuktikan dengan password valid (2026-11-02)

- **Spec / langkah:** `TC-AUTH-LP-E2E-004` TC-AUTH-LP-22 (langkah 20–25), TC-AUTH-LP-21 (langkah 26–31), dan Prerequisites "password akun `Tika Wulandari` di-set langsung oleh tim BE ke nilai `Spectra.env.LP_PASSWORD_SPACED`".
- **Spec meminta:** password Tika di-set BE ke nilai dengan spasi di awal dan akhir; login tanpa spasi tepi ditolak (TC-22) dan login dengan spasi tepi berhasil (TC-21).
- **Kenyataannya:** password tersimpan berspasi tidak dapat ada di V2. Set Password (aktivasi) dan Reset Password menolak spasi (`auth-foundation.md` §1); tidak ada jalur produksi, import, SSO, atau migrasi yang menulisnya; satu-satunya penulisnya adalah route dev `POST /dev/clients` (jawaban tim BE, iam `origin/dev`, 2026-11-02). Aturan PRD yang teramati (login-password.md D5 l.713, FLD-AUTHLP-02 l.844: password tidak di-trim, login tidak menolak spasi) adalah bahwa password valid yang diketik dengan spasi tepi tidak cocok dengan password tersimpan.
- **Karena:** state hanya disusun seperti terjadinya di produk (aturan owner). Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** Tika diaktivasi lewat flow aktivasi publik dengan `LP_PASSWORD`. TC-AUTH-LP-21 diotomasi sebagai: login dengan `" " + LP_PASSWORD + " "` menampilkan Alert "Incorrect email or password" tanpa sesi (kalau di-trim, login berhasil; kalau spasi ditolak sebagai format, pesannya lain). TC-AUTH-LP-22 dan login sukses dengan password tersimpan berspasi tidak diotomasi di e2e; perbandingan password apa adanya dijaga unit test backend pada verifikasi password login (issue iam menyusul). `setUserPassword` dan `LP_PASSWORD_SPACED` tidak dipakai lagi.
- **Diterapkan di:** skrip Login Password 004 (TC-AUTH-LP-21, TC-AUTH-LP-22).

## D-062 State sisa tulis Set Password yang putus di tengah dijaga unit test backend (2026-11-02)

- **Spec / langkah:** `TC-AUTH-ACT-E2E-020` TC-AUTH-ACT-129 (langkah 9–13) dan TC-AUTH-ACT-130 (langkah 14–17), serta fixture BE untuk `Dimas Pratama` dan `Eka Wulandari` di Prerequisites.
- **Spec meminta:** user Pending Activation dengan token Active yang statusnya diubah menjadi Activated tanpa mengonsumsi token (129), dan user Pending Activation dengan token Active yang kredensialnya sudah berisi password (130), keduanya lewat fixture BE; link dan submit langsung ditolak 409 tanpa mengubah data.
- **Kenyataannya:** tidak ada aksi user atau admin yang menghasilkan kedua state itu. Satu-satunya penulis status Activated adalah Set Password, yang juga meng-consume token; Reset Password menolak akun Pending Activation; tidak ada API admin yang mengubah status aktivasi atau menulis password. Keduanya hanya muncul bila `SetActivationPassword` putus di tengah: tiga tulisan (hash password, consume token, set Activated) lintas skema public dan tenant tanpa transaksi. User tertinggal Pending dengan password terisi dan setiap retry dijawab 409 `ACTIVATION_CREDENTIAL_ALREADY_SET`; dua request dengan token yang sama juga bisa sama-sama 200. Itu cacat backend, bukan state yang disusun e2e (jawaban tim BE 2026-11-02, issue draft `ISSUE-DRAFT-iam-activation-set-password-not-atomic.md`).
- **Karena:** state hanya disusun seperti terjadinya di produk (aturan owner). Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** TC-AUTH-ACT-129 dan TC-AUTH-ACT-130 tidak diotomasi di e2e. Perbaikan backend: ketiga tulisan dalam satu transaksi; unit test backend menjaga AUTHACT-LOGIC-01e/01f: user Activated dengan token Active dijawab 409; kredensial yang sudah berisi password dijawab 409 `ACTIVATION_CREDENTIAL_ALREADY_SET` dan token tidak di-consume. Halaman Invalid Link untuk token yang tidak lagi Active tetap diuji e2e di spec 013, 014, 021, dan 026.
- **Diterapkan di:** skrip Account Activation 020 (TC-AUTH-ACT-129, TC-AUTH-ACT-130).

## D-063 Lock 15 menit di mobile dibuat lewat tiga login mobile yang salah (2026-11-02)

- **Spec / langkah:** `TC-AUTH-LP-E2E-055` TC-AUTH-LP-65 Prerequisites ("terkunci 15 menit di mobile (fixture BE)") dan Kemampuan teknis "fixture BE untuk membuat user terkunci 15 menit di mobile".
- **Spec meminta:** fixture BE yang membuat user terkunci 15 menit di mobile tanpa kegagalan di web.
- **Kenyataannya:** di produk lock mobile terjadi lewat tiga login salah dari aplikasi mobile. API login publik (`POST /v2/iam/auth/login`, `platform: mobile`) melakukan hal yang sama, dengan token Play Integrity uji `e2e-test-integrity` yang diterima iam di stack e2e (`E2E_TEST_EVIDENCE`; provider Play Integrity belum dibangun, iam #99). Notes spec sendiri mencatat cara membuat lock "di mobile saja" tidak dijelaskan TC sumber.
- **Karena:** state disusun seperti terjadinya di produk (aturan owner). Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** Prerequisites dijalankan dengan login mobile yang salah lewat API login publik dari device mobile tersendiri, sampai backend menjawab `LOCKED_15M` (kegagalan ketiga); tanpa fixture BE dan tanpa kegagalan di web. Langkah 1–8 berjalan di web sesuai spec.
- **Diterapkan di:** skrip Login Password 055 (TC-AUTH-LP-65).

## D-064 Idle 30 hari di MFA 021 diukur dari riwayat sesi, tanpa membekukan jam dan tanpa seed `last_logout_at` (2026-11-02)

- **Spec / langkah:** `TC-AUTH-MFA-E2E-021` Prerequisites, hook `before`/`after` (bekukan jam server uji di T0, seed `last_logout_at` per user relatif terhadap T0) dan Kemampuan teknis "Manipulasi jam server uji ... serta seeding `last_logout_at` per user".
- **Spec meminta:** jam server uji dibekukan di T0 dan `last_logout_at` tiap user di-seed 31, 30, dan 29 hari sebelum T0.
- **Kenyataannya:** `auth-foundation.md` §5.1 (l.364): logout terakhir per platform tidak disimpan di kolom sendiri, tetapi diturunkan dari tabel `sessions` (`MAX(COALESCE(terminated_at, expires_at))` per user dan platform); kolom `users.last_logout_at` tidak dipakai. Riwayat itu ditulis oleh login dan logout nyata, dan umurnya digeser oleh `ageTime`. Backend tidak punya route untuk membekukan jam server (D-022).
- **Karena:** keputusan owner atas iam #97 (2026-11-02): rumus §5.1 dipertahankan dan `users.last_logout_at` tidak dipakai.
- **Keputusan:** tiap user login sekali lalu logout di browser A saat seeding, lalu riwayat sesi tenant digeser dengan `ageTime` (`sessions`, `users`) sehingga logout web terakhir berumur 31, 30, dan 29 hari. Jam server tidak dibekukan dan `last_logout_at` tidak di-seed. Batas TC-AUTH-MFA-27 diuji pada umur 30 hari ditambah detik berjalannya run (tetap ≥30 hari), bukan tepat 30 hari 0 detik.
- **Diterapkan di:** skrip MFA 021 (Prerequisites).

## D-065 Baseline Changelog File Manager 062 dibaca sesudah setup, bukan nol (2026-11-02)

- **Spec / langkah:** `TC-GS-FILEMGR-E2E-062` Prerequisites "Baseline log" dan langkah 21–22 (Log Suspended), serta langkah Log Expired yang sama.
- **Spec meminta:** baseline nol untuk file bersuffix `{runId}-062` di Changelog File Manager; langkah 22 memverifikasi tidak ada entri baru dengan empty state "No results found".
- **Kenyataannya:** `legacy-photo-{runId}-062.jpeg` masuk Recycle Bin lewat Delete File Manager yang nyata (satu-satunya jalan ke Recycle Bin), dan Delete itu menulis satu baris Changelog `Delete` untuk file tersebut. Sesudah setup, pencarian `{runId}-062` sudah memuat satu baris, sehingga baseline nol tidak bisa terpenuhi. Ketiga aksi tulis saat Suspended tetap ditolak dan tidak menulis baris baru.
- **Karena:** state disusun seperti terjadinya di produk (aturan owner); maksud langkah 22 adalah "tidak ada entri baru". Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** baseline adalah jumlah baris Changelog untuk pencarian `{runId}-062` yang dibaca sesudah setup (baris Delete dari setup sudah tercatat) dan sebelum aksi tulis saat Suspended. Langkah 22 memverifikasi jumlah baris sama dengan baseline (tidak ada entri baru dari aksi yang ditolak), bukan empty state.
- **Diterapkan di:** skrip File Manager 062.

## D-066 FILEMGR 024 gambar tidak tersedia mengikuti aturan galeri in-page (2026-11-02)

- **Spec / langkah:** `TC-GS-FILEMGR-E2E-024`, TC-53, langkah 5–8.
- **Spec meminta:** gambar yang tidak tersedia dibuka di tab baru, tanpa toast.
- **Kenyataannya:** PRD file-manager, aturan preview in-page (l.399) dan V-11: gambar dibuka di galeri in-page, bukan tab baru.
- **Karena:** keputusan koordinator (didelegasikan owner) 2026-11-02, dicatat sebagai G21 di tagsamurai-slicing `plans/_program/gs-triage/ui-items.md`.
- **Keputusan:** perilaku galeri in-page berlaku untuk gambar yang tidak tersedia: galeri menutup, toast T-13 tampil, dan daftar di-refetch. Tidak ada tab baru.
- **Diterapkan di:** skrip File Manager 024 (sudah meng-assert perilaku ini, commit e0e7272f di feat/connect-api-b).

## D-067 Klik backdrop tidak menutup modal Changelog (2026-11-02)

- **Spec / langkah:** `TC-GS-DIV-E2E-053` TC-GS-DIV-211 langkah 39–40.
- **Spec meminta:** klik area gelap di luar modal menutup modal Changelog: Division.
- **Kenyataannya:** modal Changelog tetap terbuka setelah klik backdrop. Spec lain untuk modal Changelog yang sama meminta hal sebaliknya dan lolos: `TC-GS-POS-E2E-038` TC-GS-POS-203 langkah 44–45 dan `TC-GS-FILEMGR-E2E-044` TC-GS-FILEMGR-174.
- **Karena:** `prd-conventions.md` §9.10 Changelog Modal (l.1720): "**Klik backdrop (area di luar modal) tidak menutup modal** — menutup hanya lewat icon `[✕]` atau `Esc`." PRD division §5 Global Table Rules (l.672) merujuk modal "Changelog: Division" ke §9.10; §24.5 (l.2631) berlaku untuk semua modal. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** langkah 40 memverifikasi modal Changelog tetap terbuka setelah klik backdrop, lalu modal ditutup lewat icon `[✕]`.
- **Diterapkan di:** skrip Division 053 (TC-GS-DIV-211).

## D-068 ACTLOG 031 Object Role mengikuti nama tab role (2026-11-02)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-031` TC-GS-ACTLOG-174, `spec.md` l.37 dan l.53 (tagsamurai-slicing `apps/e2e/specs/GlobalSettings/ActivityLog/TC-GS-ACTLOG-E2E-031-*`).
- **Spec meminta:** Role `Role {runId}-031` yang di-seed oleh Sari Dewi tercatat di Activity Log dengan Object `Role & Permission`; opsi filter Object memuat `Role & Permission`.
- **Kenyataannya:** PRD role (`global-settings/role/PRD/role.md`): `object_path` = "`Total Control` · `Read Only` · `System Role` (nilai kolom Object §8.5–§8.6)" (l.1885) dan "memakai nama tab ..., bukan nama menu `Role & Permission`" (l.1891). Global Settings juga tidak punya operasi create role: baris role fixed dan tidak ada +Add (`role.md` l.1238, l.2144 "hardcoded di kode"), dan API role (`API/low-level-design.md`) hanya memuat list/options/export serta Assign/Remove user dan access level, tanpa route create role. Role `Role {runId}-031` tidak bisa dibuat lewat produk.
- **Karena:** PRD menang atas spec. Keputusan koordinator (didelegasikan owner) 2026-11-02.
- **Keputusan:** skrip meng-assert Object `Total Control` untuk Role yang di-seed, mengikuti nama tab di PRD, bukan `Role & Permission`.
- **Diterapkan di:** skrip Activity Log 031 (TC-GS-ACTLOG-174), commit 26e7dbbc di feat/connect-api-b (tagsamurai-slicing-b).
## D-065 Setup Column Client berlaku setelah Save: tabel di balik modal tidak berubah sebelum [Save] (2026-11-03)

- **Spec / langkah:** `TC-AC-ACC-E2E-245`, `257`, `258`, `260`, `294`, `295`, `296`, `297` (TC-AC-ACC-825, 743, 744, 746, 696, 407, 688, 689, 690, 691).
- **Spec meminta:** TC menulis kolom yang dicentang/dilepas, diseret, atau di-reset di modal Setup Column langsung terlihat pada tabel di balik modal sebelum `[Save]`, mengutip `prd-conventions.md` §9.3.
- **Kenyataannya:** tabel di balik modal tidak berubah sampai `[Save]`; menutup modal dengan `[✕]` atau `Esc` tanpa Save membuang perubahan. Sama seperti D-008. Teks `prd-conventions.md` §9.3 ("di-preview langsung di tabel (tabel di balik modal merefleksikan state sementara ini secara real-time)") berbeda dari perilaku ini dan belum diubah (berlaku untuk modul lain juga).
- **Karena:** keputusan user 2026-11-03 (jalur "UI tidak preview") atas temuan F-1 `report-e2e-audit.md` (`prd-harness/work-items/ac-client`), selaras dengan keputusan user 2026-11-02 yang sudah tertulis di Notes spec-spec ini.
- **Keputusan:** spec Client mengikuti UI: kolom masih tampil/urutan tidak berubah di tabel di balik modal sampai `[Save]`. Live Preview di dalam popup tetap terpisah.
- **Diterapkan di:** Notes dan asersi spec 245, 257, 258, 260, 294, 295, 296, 297 (sudah sesuai). `tc-client.md` (10 TC) dan `prd-conventions.md` §9.3 belum diselaraskan: menunggu keputusan cakupan, lihat `report-e2e-audit.md` F-1.

## D-069 Request langsung dengan product di luar daftar tidak diuji di e2e (2026-11-03)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-057` TC-GS-ACTLOG-217 (langkah 1 sampai 5).
- **Spec meminta:** request langsung ke endpoint daftar Session dengan parameter produk `fams` disisipkan; server menjawab sukses, mengabaikan nilai itu, dan hanya mengembalikan baris platform dan Global Settings.
- **Kenyataannya:** `POST /v2/analytics-reporting/session-logs/list` menjawab 422 `Invalid request body` (`product` harus salah satu dari `admin_console`, `global_settings`).
- **Karena:** klien FE tidak bisa mengirim nilai `product` di luar daftar, jadi skenarionya tidak terjadi di produksi dan tidak mewakili bug nyata. Bug yang sebenarnya ada di endpoint pembuatan log, yang menulis field `product` salah.
- **Keputusan:** TC-GS-ACTLOG-217 dikeluarkan dari e2e; tidak ada perubahan di backend. Yang diuji adalah penulisan `product` oleh endpoint pembuatan log, lewat test get list yang sudah ada. Keputusan owner, disampaikan lewat sesi BE dan dikonfirmasi owner pada 2026-11-03.
- **Diterapkan di:** skrip 057: blok TC-GS-ACTLOG-217 ditandai `// @spec-decision: D-069 TC-GS-ACTLOG-217` dan tanpa step; TC-GS-ACTLOG-215 dan 216 tetap.

## D-070 Filter Date adalah satu kalender rentang: satu tanggal terpilih berarti hari itu saja (2026-11-03)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-039` TC-GS-ACTLOG-77 (langkah 15 sampai 26).
- **Spec meminta:** hanya tanggal mulai diisi: filter terbuka ke sisi lainnya, dari tanggal itu dan seterusnya (PRD FI-04); hanya tanggal akhir diisi: sampai tanggal itu (PRD FI-05).
- **Kenyataannya:** filter Date (FilterContainer `type: 'date'`) adalah satu DatePicker mode rentang dengan satu input. Klik pertama selalu menjadi tanggal mulai, sehingga tanggal akhir saja tidak dapat dimasukkan. Satu tanggal yang dipilih menghasilkan rentang hari itu (dokumentasi komponen: "one picked day covers that day"; `[hari itu 00:00:00.000, 23:59:59.999]`). Rentang terbuka ke satu sisi tidak didukung komponen, dan kode aplikasi tidak mengubah nilai itu.
- **Karena:** perilaku komponen Wangs UI, bukan kode aplikasi.
- **Keputusan:** perilaku komponen menang. Memilih satu tanggal berarti hari itu saja. FI-04 dan FI-05 (rentang terbuka satu sisi) tidak diimplementasikan dan tidak diuji; TC-GS-ACTLOG-77 keluar dari e2e. Perilaku "hari itu saja" sudah dijaga TC-GS-ACTLOG-74 dan TC-GS-ACTLOG-75 (rentang dengan tanggal mulai dan akhir yang sama). Keputusan owner, disampaikan di sesi integrasi 2026-11-03.
- **Diterapkan di:** skrip 039: blok TC-GS-ACTLOG-77 ditandai `// @spec-decision: D-070 TC-GS-ACTLOG-77` dan tanpa step.

## D-071 Pindah halaman di tengah Guided Tour dilakukan lewat URL, bukan klik sidebar atau tab (2026-11-04)

- **Spec / langkah:** `TC-GS-BRAND-E2E-008` TC-GS-BRAND-24 (langkah 24 dan 26); `TC-GS-DIV-E2E-005` TC-GS-DIV-15 (pindah ke tab Position lalu kembali ke Division saat walkthrough terbuka).
- **Spec meminta:** mengklik item sidebar (Activity Log) atau tab (Position) selagi walkthrough terbuka, lalu walkthrough tertutup tanpa menyimpan flag seen (PRD §16.3 "Resize / navigasi = tutup tanpa set flag seen").
- **Kenyataannya:** selama Guided Tour terbuka, halaman di belakangnya tidak bisa diklik; hanya elemen yang disorot yang bisa. Klik di area gelap sama dengan Skip dan menyimpan flag seen (wangs-ui 1.4.0-alpha.178).
- **Karena:** keputusan owner atas perilaku komponen Guided Tour Wangs UI (2026-11-04, disampaikan lewat Wangs-UI Coordinator). Dua aturan itu bertabrakan di PRD: blokir klik dan "navigasi menutup tur".
- **Keputusan:** blokir klik tetap. Berpindah halaman di tengah tur dilakukan lewat URL langsung atau Back browser; layar yang di-unmount menutup tur tanpa menyetel seen, dan skrip membaca bahwa flag seen tidak tersimpan. Tur milik halaman tujuan ditandai seen lebih dulu supaya langkah berikutnya (klik sidebar) bisa berjalan. Semua aturan lain pada kedua TC tetap berlaku. Dicatat atas permintaan pengguna sesi integrasi pada 2026-11-04.
- **Diterapkan di:** skrip Brand 008 TC-GS-BRAND-24 dan Division 005 TC-GS-DIV-15, ditandai `// @spec-decision: D-071`. Position 006 tidak menyimpang dari spec: kunjungan tab dibuat dengan memuat ulang halaman, bukan klik tab saat tur terbuka.

## D-072 Hover Position Name tidak menampilkan border primary (2026-11-04)

- **Spec / langkah:** `TC-GS-POS-E2E-001` TC-GS-POS-293 (langkah 78 dan 79).
- **Spec meminta:** field Position Name menampilkan border primary saat pointer berada di atasnya.
- **Kenyataannya:** preset `inputgroup` (fixedasset) punya outline normal `outline-variant` dan outline primary saat focus-within; tidak ada state hover.
- **Karena:** PRD tidak memiliki baris tentang border hover. Konvensi umum: hover menggelapkan border netral dan warna primary dipakai untuk focus. Keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04).
- **Keputusan:** komponen tetap. Langkah hover tidak diuji; fokus diuji lewat ring (langkah 81).
- **Diterapkan di:** skrip `TC-GS-POS-E2E-001`, ditandai `// @spec-decision: D-072 TC-GS-POS-293`.

## D-073 Daftar dua nama di dialog tidak punya scroll (2026-11-04)

- **Spec / langkah:** `TC-GS-FILEMGR-E2E-022` TC-GS-FILEMGR-96 (langkah 18).
- **Spec meminta:** daftar nama pada dialog Permanently Delete bisa di-scroll.
- **Kenyataannya:** Ul foundation menambah ScrollArea hanya bila item melebihi `maxVisibleItems`; dua nama tidak melewatinya.
- **Karena:** daftar baru bisa di-scroll bila isinya melebihi batas tampil; PRD §2 (tabel placeholder, "scrollable, jumlah tampil dibatasi") bermaksud sama. Keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04).
- **Keputusan:** kedua nama tampil utuh sebagai asersi; asersi scroll hanya untuk daftar di atas batas.
- **Diterapkan di:** skrip `TC-GS-FILEMGR-E2E-022`, ditandai `// @spec-decision: D-073 TC-GS-FILEMGR-96`.

## D-074 Ukuran px Illustration empty state tidak diuji di e2e (2026-11-04)

- **Spec / langkah:** `TC-GS-DIV-E2E-003` TC-GS-DIV-6 langkah 4 dan TC-GS-DIV-7 langkah 11; `TC-GS-DIV-E2E-054` TC-GS-DIV-191 langkah 11 dan TC-GS-DIV-192 langkah 3.
- **Spec meminta:** Illustration empty state berukuran 100x100.
- **Kenyataannya:** EmptyState Wangs UI memakai ikon yang ukurannya mengikuti prop `size` (preset `size-8`, 32 px).
- **Karena:** ini detail visual dari prd-conventions §31.3b dan desain sistem komponen; wilayah visual/Chromatic. Keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04).
- **Keputusan:** e2e menegaskan empty state tampil dengan ilustrasi atau ikon, judul, dan deskripsi yang benar, tanpa ukuran.
- **Diterapkan di:** skrip 003 dan 054, ditandai `// @spec-decision: D-074`.

## D-075 NumberInput menjepit nilai ke batas aplikasi: `-3` terbaca `0` (2026-11-03)

- **Spec / langkah:** `TC-GS-BRAND-E2E-036` TC-GS-BRAND-278 (langkah 5-6 dan 16-17, filter Used By Items).
- **Spec meminta:** karakter yang tidak valid dibuang saat diketik: `-3` terbaca `3`, `2.5` terbaca `25`.
- **Kenyataannya:** NumberInput kembali ke perilaku default (wangs-ui 1.4.0-alpha.174): batas datang dari props aplikasi (min 0, mode bilangan bulat) dan komponen menjepit nilainya, jadi `-3` terbaca `0`, `2.5` dibulatkan menjadi `3`, dan `2,5` terbaca `25` (diamati lewat setRange pada alpha.178; spec meminta `-3` terbaca `3`, `2.5` terbaca `25`).
- **Karena:** keputusan owner 2026-11-03 bahwa perilaku komponen berlaku; dikonfirmasi Wangs UI coordinator (2026-11-04).
- **Keputusan:** skrip mengikuti hasil komponen. Catatan: CustomFieldUser 024 (`-12.5` terbaca `125` pada field Numeric) tidak termasuk keputusan ini.
- **Pembaruan 2026-11-05 (alpha.191):** NumberInput dengan min 0 kini menolak tanda minus saat diketik, jadi `-3` terbaca `3` (sama dengan permintaan spec); nilai `2.5` dan `2,5` mengikuti hasil komponen yang terbaca di run. Aturan keputusan tetap: skrip mengikuti hasil komponen (Brand 036, Measurement 038).
- **Diterapkan di:** skrip `TC-GS-BRAND-E2E-036` dan `TC-GS-UOM-E2E-038`, ditandai `// @spec-decision: D-075 TC-GS-BRAND-278`.

## D-076 Presentasi mobile 390px tidak ada di komponen web dan keluar dari run web (2026-11-04)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-007`: TC-GS-ACTLOG-24 langkah 4 dan 6; TC-GS-ACTLOG-25 langkah 9-15; TC-GS-ACTLOG-26 langkah 18-23; TC-GS-ACTLOG-140 langkah 25 dan 29.
- **Spec meminta:** di viewport mobile (390 x 844): Step 2 Guided Tour menyorot tombol [⋯] di toolbar; tooltip tampil sebagai bottom sheet mini; daftar Session dan User Action tampil sebagai card; Download berada di dalam overflow [⋯].
- **Kenyataannya:** DataTable dan LogTable web memakai baris tabel di semua lebar; toolbar tetap Search | Filter | Download; GuidedTour hanya punya satu presentasi (popover).
- **Karena:** kartu responsif, overflow [⋯], dan bottom sheet adalah presentasi mobile yang tidak ada di komponen web; membangunnya menambah fitur besar di library, bukan memperbaiki gap. Keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04).
- **Keputusan:** bagian-bagian itu keluar dari run web dan ditandai mobile-only; spec tetap disimpan untuk platform mobile. Yang tetap diuji di web: tur dibuka dan berpindah langkah, tab Session dan User Action, serta file hasil Download (tombol Download dipakai langsung).
- **Diterapkan di:** skrip 007: lima blok ditandai `// @spec-decision: D-076` dan tanpa step.

## D-077 [Clear Field] dan [Apply] sebaris: "kiri" dan "kanan" adalah urutan tombol, bukan tepi panel (2026-11-04)

- **Spec / langkah:** `TC-GS-POS-E2E-029` TC-GS-POS-159 (langkah 10).
- **Spec meminta:** [Clear Field] di kiri dan [Apply] di kanan panel Filter; skrip sebelumnya membaca "kiri" sebagai tepi kiri panel.
- **Kenyataannya:** FilterContainer menaruh kedua tombol dalam satu baris, [Clear Field] langsung di kiri [Apply], grupnya rata kanan.
- **Karena:** prd-conventions §9.8 (keputusan 2026-09-07) memakai kata "kiri" dan "kanan" untuk urutan dua tombol yang berjejeran. Klarifikasi owner; keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04).
- **Keputusan:** komponen tetap. Asersi: [Clear Field] dan [Apply] sebaris, [Clear Field] langsung di kiri [Apply]. Tidak ada asersi posisi tepi panel.
- **Diterapkan di:** skrip `TC-GS-POS-E2E-029`, ditandai `// @spec-decision: D-077 TC-GS-POS-159`.

## D-078 Toast kegagalan tulis tidak punya tombol [Try Again] (2026-11-04)

- **Spec / langkah:** `TC-GS-ROLE-E2E-070` TC-GS-ROLE-306 langkah 14; `TC-GS-ROLE-E2E-073` TC-GS-ROLE-309 langkah 23.
- **Spec meminta:** toast `Connection problem. Please try again.` memuat tombol `[Try Again]`.
- **Kenyataannya:** aplikasi tidak punya tombol itu pada toast (PRD override 2026-10-17, tercatat di decisions.md fitur); wrapper Toast hanya membaca judul, pesan, ikon, dan tombol tutup, jadi tidak ada yang bisa dibaca.
- **Karena:** bukan celah wrapper; tidak ada tombol yang dirender. Keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04, CD-013).
- **Keputusan:** e2e menegaskan toast dan teksnya; tombol `[Try Again]` keluar dari e2e.
- **Diterapkan di:** skrip 070 dan 073, ditandai `// @spec-decision: D-078`.

## D-079 Warna danger dan jarak 4px pesan error inline adalah detail visual (2026-11-04)

- **Spec / langkah:** `TC-GS-ROLE-E2E-024` TC-GS-ROLE-24 langkah 8-9; `030`, `031`, `032` (alert inline danger); `034`, `036` (error `You must pick a user`, danger, di atas tombol footer).
- **Spec meminta:** teks error inline berwarna danger, rata kanan, 4px di atas tombol footer.
- **Kenyataannya:** tidak ada wrapper Text yang membaca severity atau jarak.
- **Karena:** warna dan jarak adalah detail visual milik preset; wilayah tes visual, bukan e2e. Keputusan Wangs UI coordinator, didelegasikan owner (2026-11-04, CD-012).
- **Keputusan:** e2e menegaskan teks error lewat wrapper field/alert; warna dan jarak tidak diasersi.
- **Diterapkan di:** skrip 024, 030, 031, 032, 034, 036, ditandai `// @spec-decision: D-079`.

## D-080 Walkthrough terbuka menutupi sidebar: klik burger/sidebar bukan jalur e2e untuk "pindah halaman" (2026-11-04)

- **Spec / langkah:** `TC-GS-ACTLOG-E2E-006` TC-GS-ACTLOG-22 langkah 24 (pada viewport 768: klik `Toggle sidebar`, lalu `User` di sidebar, saat walkthrough terbuka).
- **Spec meminta:** dengan walkthrough terbuka, user membuka halaman lain lewat sidebar; walkthrough menutup dan flag seen tidak menjadi true.
- **Kenyataannya:** overlay walkthrough (`fixed inset-0 z-40`, `aria-hidden`) adalah backdrop GuidedTour. Backdrop itu ditambahkan di wangs-ui alpha.178 (CD-002, dikonfirmasi owner): selama tour tampil, halaman di belakangnya tidak menerima klik, dan klik pada halaman yang diredupkan = skip tour. Di alpha.174 backdrop belum ada, jadi klik burger dulu klik sungguhan. Burger dan sidebar tertutup, user tidak bisa mengkliknya (kasus CD-003 milik Wangs-UI Coordinator). Bukti: TestSpectra 1.2.39, `--break-on-failure`, `elementFromPoint` di tengah `Toggle sidebar` = overlay `DIV aria-hidden`; klik overlay menutup walkthrough, URL tetap `/global-settings/activity-log/session`.
- **Karena:** perilaku komponen GuidedTour disengaja; yang berubah adalah jalur klik pada spec. Tidak boleh `{ force: true }`.
- **Dikoreksi (2026-11-04, bukti run):** klik overlay walkthrough sama dengan Skip dan menyimpan flag seen (`localStorage gs-activity-log = true`, dibaca langsung setelah klik, 2 run; sejalan dengan Brand 008 TC-21 dan Division 005 TC-12). Jadi jalur "tutup lewat overlay, lalu klik sidebar" tidak bisa memenuhi langkah 26 ("flag seen tidak true"): flag sudah true karena Skip, bukan karena pindah halaman. Jalur navigasi browser ke halaman User saat walkthrough masih terbuka (muat ulang penuh) memenuhi langkah 24-28 utuh (2 dari 2 run): walkthrough hilang, flag false, kembali ke Activity Log membuka walkthrough di Step 1.
- **Keputusan:** jalur B. Dengan walkthrough terbuka, halaman lain dibuka lewat navigasi browser ke halaman User (muat ulang penuh); langkah klik burger/sidebar tidak dijalankan karena overlay menutupinya dan klik overlay = Skip yang menyimpan flag. Langkah 24-28 diasersi seperti tertulis: walkthrough tertutup, sidebar `User` aktif (burger diklik dulu pada viewport 768 agar label terlihat), flag seen false, kembali ke Activity Log membuka walkthrough di Step 1 sendiri. Keputusan user sesi integrasi (2026-11-04, "006 pake B"), sejalan dengan CD-003 (navigasi di tengah tour lewat URL atau navigasi browser; layar yang di-unmount menutup tour tanpa menyimpan `seen`).
- **Diterapkan di:** skrip 006, langkah 24, ditandai `// @spec-decision: D-080`.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-002, CD-003), 2026-11-04; keputusan ada di keempat sesi, tidak menunggu owner.

## D-081 Overlay row action (Menu) tidak punya backdrop, dan itu bukan perilaku app (2026-11-05)

- **Spec / langkah:** `TC-GS-UOM-E2E-028` TC-GS-UOM-333 langkah 5 (overlay row action tanpa backdrop), dan setiap spec lain yang meminta assertion ketiadaan backdrop pada Menu.
- **Spec meminta:** overlay row action tampil tanpa backdrop.
- **Kenyataannya:** Menu Wangs UI tidak pernah punya backdrop di layar mana pun; tidak ada prop atau konfigurasi app yang mengubahnya, sehingga tidak ada perilaku app yang bisa diuji.
- **Karena:** desain komponen yang sama di semua layar (CD-018).
- **Keputusan:** langkah itu tidak diasersi di e2e.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-018), 2026-11-05.
- **Diterapkan di:** skrip Measurement 028, ditandai `// @spec-decision: D-081`.

## D-082 Warna latar header AccordionItem saat hover adalah detail visual (2026-11-05)

- **Spec / langkah:** `TC-GS-UOM-E2E-044` TC-GS-UOM-298 langkah 18-19.
- **Spec meminta:** latar header item Accordion berubah saat di-hover.
- **Kenyataannya:** warna hover milik preset Wangs UI, tidak diatur app.
- **Karena:** detail visual, wilayah tes visual, bukan e2e; sama dengan D-079 (CD-012). Keputusan CD-019.
- **Keputusan:** warna hover tidak diasersi.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-019), 2026-11-05.
- **Diterapkan di:** skrip Measurement 044, ditandai `// @spec-decision: D-082`.

## D-083 Arah atau rotasi ikon expand AccordionItem adalah detail visual; state-nya diasersi (2026-11-05)

- **Spec / langkah:** `TC-GS-UOM-E2E-044` TC-GS-UOM-298 langkah 21 dan 23; `TC-GS-UOM-E2E-053` TC-GS-UOM-200 langkah 20 dan 23.
- **Spec meminta:** ikon expand menunjuk arah tertentu saat collapsed dan expanded.
- **Kenyataannya:** rotasi ikon milik preset Wangs UI.
- **Karena:** detail visual (CD-020); yang bermakna adalah state item.
- **Keputusan:** arah ikon tidak diasersi; state diasersi dengan `item.shouldBeExpanded()` / `shouldNotBeExpanded()`.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-020), 2026-11-05.
- **Diterapkan di:** skrip Measurement 044 dan 053, ditandai `// @spec-decision: D-083`.

## D-084 Kolom seleksi dan kolom Actions tidak pernah sortable (2026-11-05)

- **Spec / langkah:** `TC-GS-UOM-E2E-040` TC-GS-UOM-152 langkah 1-3 (tidak ada ikon sort pada header Checkbox dan Actions).
- **Spec meminta:** header kolom Checkbox dan Actions tidak menampilkan ikon sort saat di-hover.
- **Kenyataannya:** kedua kolom itu milik DataTable sendiri dan tidak pernah sortable; ikon sort hanya ada pada kolom data yang `sortable`. Tidak ada konfigurasi app yang mengubahnya.
- **Karena:** desain komponen (CD-021).
- **Keputusan:** langkah itu tidak diasersi; sort kolom data tetap diasersi lewat `isColumnSortable(header)`.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-021), 2026-11-05.
- **Diterapkan di:** skrip Measurement 040, ditandai `// @spec-decision: D-084`.

## D-085 Toast: satu slot, toast baru menggantikan yang tampil; "maksimal 3 dan antrean" ditolak (2026-11-05)

- **Spec / langkah:** `TC-GS-UOM-E2E-021` TC-GS-UOM-340 langkah 35-37, dan setiap spec lain yang meminta tumpukan toast terbatas dengan antrean.
- **Spec meminta:** paling banyak 3 toast sukses tampil bersamaan; toast ke-4 antri dan tampil setelah salah satu hilang.
- **PRD:** Measurement §4 item 14 menyerahkan perilaku toast ke `toast_copy()`; `foundation/functions/toast-copy.md` Aturan Terkunci #12 (dirujuk `prd-conventions.md` §22): "Toast baru menggantikan toast yang sedang tampil (tidak ada stacking, hanya 1 slot aktif di kanan bawah)".
- **Kenyataannya:** Toast Wangs UI punya `ToastHandle.replace(message)` yang mengganti semua toast yang tampil; batas 3 dan antrean tidak ada di komponen.
- **Karena:** §2 `spec-conflicts`: aturan PRD berlaku di seluruh app dan sudah dimiliki komponen (`replace`), sedangkan batas 3 + antrean adalah perilaku baru untuk satu spec (CD-022).
- **Keputusan:** spec 3+antrean ditolak; langkah 36-37 menegaskan satu slot: setelah 4 submit cepat tepat satu toast `Success, unit has been created.` tampil. Bila app menumpuk toast (`show()` bukan `replace()`), itu temuan `ui`, bukan alasan untuk D-entry lain.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-022), 2026-11-05.
- **Diterapkan di:** skrip Measurement 021, ditandai `// @spec-decision: D-085`.

## D-086 Daftar dial code PhoneInput milik komponen, tidak diuji di e2e (2026-11-05)

- **Spec / langkah:** `TC-GS-NLU-E2E-024` TC-GS-NLU-502 langkah 6 (dropdown dial code tanpa opsi kosong), dan setiap spec lain yang mengasersi isi daftar dial code.
- **Spec meminta:** dropdown kode negara tidak memuat opsi kosong.
- **Kenyataannya:** daftar dial code dibangun PhoneInput Wangs UI dari libphonenumber (semua negara); app tidak mengaturnya.
- **Karena:** perilaku milik komponen, dijaga test Layer 3 Wangs UI (`phoneInput.helper.test.ts`: tanpa opsi kosong, tanpa negara ganda) (CD-029).
- **Keputusan:** langkah itu tidak diasersi di e2e.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-029), 2026-11-05.
- **Diterapkan di:** skrip NonLoginUser 024, ditandai `// @spec-decision: D-086`.

## D-087 Delete langsung unit yang dipakai: kontrak menjawab 200 dengan baris `blocked`/`in_use`, bukan respons gagal (2026-11-05)

- **Spec / langkah:** `TC-GS-UOM-E2E-070` TC-GS-UOM-238 (request Delete langsung untuk unit yang Used By > 0).
- **Spec meminta:** request Delete langsung untuk unit yang dipakai mendapat respons gagal.
- **Kenyataannya:** kontrak (`global-settings/measurement/API/openapi.yaml` L267, L298, L694-700) mendefinisikan Delete sebagai operasi per baris: jawaban `200` dengan hasil `blocked` dan `reason: in_use` untuk baris yang dipakai (pesan `0 deleted, 1 skipped`), dan unit tidak terhapus.
- **Karena:** perilaku backend mengikuti kontrak API; spec menyederhanakan "ditolak" menjadi "respons gagal".
- **Keputusan:** skrip menegaskan jawaban kontrak (`200`, baris `blocked`/`in_use`) dan bahwa unit masih ada. Makna "ditolak" pada spec terpenuhi.
- **Diputuskan oleh:** sesi Integration, 2026-11-05 (kontrak API; tidak menyangkut komponen).
- **Diterapkan di:** skrip Measurement 070, ditandai `// @spec-decision: D-087`.

## D-088 Layout Detail User dan Non-Login User mengikuti prd-overrides 2026-10-20 (2026-11-05)

- **Spec / langkah:** setiap spec GlobalSettings/User dan GlobalSettings/NonLoginUser yang mengasersi header Detail lama: `TC-GS-USER-E2E-009` TC-GS-USER-1002 langkah 46, `-038` langkah 40, `-059` TC-GS-USER-335 langkah 4 dan TC-GS-USER-340 langkah 63, `-061` TC-GS-USER-356 langkah 5, 9, 13, `-062` (seluruhnya), `-147` TC-GS-USER-925 langkah 38, `-170` TC-GS-USER-1123 langkah 14, `-176` TC-GS-USER-1134 langkah 30.
- **Spec meminta:** header Detail memuat Avatar + Full Name (inisial pada avatar kosong), badge Active/Inactive di bawah nama, Employee ID sebagai subtitle, General Information tanpa Full Name dan Status, dan selector `Viewing: [Product ▾]`.
- **PRD:** user §4.2 Page: User Detail dan non-login-user §4.2d menulis layout lama itu; `plans/_program/prd-overrides.md` (baris global-settings/user, global-settings/non-login-user; diputuskan Zain Kurnia, 2026-10-20) menggantinya: judul header `User Profile` + switch Active + `[⋯]`; avatar adalah ImagePicker inline (Edit/Delete miliknya, empty state bawaan ImagePicker, tanpa inisial) di kiri grid `General Information` 3 kolom berisi `Name`, `Employee ID`, `Status` dan field General Information lain; `Custom Fields` section collapsible di bawahnya; selector `Viewing: [Product ▾]` tidak dibangun.
- **Karena:** §1 `spec-conflicts`: keputusan owner yang tercatat menang atas PRD sampai PRD diperbarui; spec ditulis dari PRD lama.
- **Keputusan:** langkah header diasersi menurut layout override (judul `User Profile`, Name dan Status di General Information, avatar kosong = empty state ImagePicker). Blok selector `Viewing:` (spec 062, TC-GS-USER-1002 langkah 46, TC-GS-USER-925 langkah 38) tidak punya langkah di e2e karena fiturnya tidak ada; bila owner membangunnya kembali, D-entry ini dicabut.
- **Diputuskan oleh:** sesi Integration, 2026-11-05, menerapkan prd-overrides 2026-10-20 (owner).
- **Diterapkan di:** skrip User 009, 038, 059, 061, 062, 147, 170, 176 dan NonLoginUser yang mengasersi header Detail, ditandai `// @spec-decision: D-088`.

## D-089 Format tanggal 4 digit tahun yang tidak ditawarkan General Settings diganti opsi enum yang setara urutannya (2026-11-05)

- **Spec / langkah:** `TC-GS-USER-E2E-002` TC-GS-USER-18 (prasyarat Date Format `DD/MM/YYYY`), `TC-GS-USER-E2E-154` langkah 2, 7, 11, 16, 19 (format `MM/DD/YYYY`), dan setiap spec lain yang menyetel Date Format di luar enum General Settings.
- **Spec meminta:** General Settings Date Format `DD/MM/YYYY` atau `MM/DD/YYYY`, lalu tanggal tampil dengan format itu.
- **PRD:** general-settings §4.3b menawarkan 5 opsi: `dd/MM/yy` (default), `M/d/yy`, `dd MMM yy`, `DDD, MMM dd, yy`, `DDD, MMM dd, yyyy`; kontrak (`global-settings/general-settings/API/openapi.yaml` L283, L322) dan LLD V-06 menolak nilai lain (`Invalid date format`). Tidak ada `DD/MM/YYYY` maupun `MM/DD/YYYY`.
- **Karena:** §2 `spec-conflicts`: nilai spec tidak bisa disetel (backend menolaknya); maksud langkah (tanggal mengikuti General Settings, day-first atau month-first) tetap teruji dengan opsi enum yang urutannya sama.
- **Keputusan:** `DD/MM/YYYY` diganti `dd/MM/yy`, `MM/DD/YYYY` diganti `M/d/yy`; asersi membaca format opsi pengganti itu (nilai yang dihitung dari cap waktu backend pada zona yang disetel).
- **Diputuskan oleh:** sesi Integration, 2026-11-05 (enum General Settings; tidak menyangkut komponen).
- **Diterapkan di:** skrip User 002 dan 154, ditandai `// @spec-decision: D-089`.

## D-090 Download di atas 5.000 baris mengikuti error-handling §10.1: loading screen lalu langsung terunduh, tanpa job background (2026-11-05)

- **Spec / langkah:** `TC-GS-USER-E2E-077` TC-GS-USER-462 langkah 1-7, dan setiap spec lain yang meminta Download/Export di atas 5.000 baris sebagai job background.
- **Spec meminta:** Download lebih dari 5.000 baris berjalan sebagai job background: toast informasional, lalu notifikasi baru di Notification Center dengan tombol [Download] saat berkas siap.
- **PRD:** `foundation/process/prd-process/error-handling-convention.md` §10.1 (definisi kanonik, wajib dirujuk modul): Download/Export di atas threshold **tidak** memakai job background; loading screen sampai berkas siap, lalu berkas langsung terunduh; tidak ada toast informasional "Preparing…", tidak ada notifikasi in-app, dan Download sukses tidak menampilkan toast. Pola job background + notifikasi hanya untuk Import/Bulk action.
- **Karena:** §2 `spec-conflicts`: konvensi lintas modul berlaku; spec mengikuti versi lama F-BORROW-17 yang sudah digantikan §10.1.
- **Keputusan:** langkah job background, toast informasional, dan notifikasi [Download] ditolak. Langkah diasersi menurut §10.1: Download as CSV pada tabel lebih dari 5.000 baris langsung mengunduh berkas berisi semua baris, tanpa toast sukses, dan tanpa notifikasi baru.
- **Diputuskan oleh:** sesi Integration, 2026-11-05 (konvensi PRD; tidak menyangkut komponen).
- **Diterapkan di:** skrip User 077, ditandai `// @spec-decision: D-090`.

## D-091 Lebar SearchButton saat terbuka adalah detail visual preset, tidak diuji di e2e (2026-11-05)

- **Spec / langkah:** `TC-GS-USER-E2E-078` TC-GS-USER-470 langkah 21 ("search bar melebar"), dan setiap spec lain yang mengasersi lebar box Search.
- **Spec meminta:** box Search melebar saat dibuka.
- **Kenyataannya:** lebar box SearchButton Wangs UI ditentukan preset komponen; spec tidak memberi angka lebar.
- **Karena:** detail visual milik preset komponen, sama dengan CD-012 (CD-031).
- **Keputusan:** langkah lebar tidak diasersi; langkah itu diwakili `shouldBeOpen()`. Tombol reset ✕ (langkah 25) tetap diasersi dengan `shouldBeClearVisible()` / `shouldNotBeClearVisible()` (alpha.191).
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-031), 2026-11-05.
- **Diterapkan di:** skrip User 078, ditandai `// @spec-decision: D-091`.

## D-092 State hover Button adalah gaya visual komponen, tidak diuji di e2e (2026-11-05)

- **Spec / langkah:** `TC-GS-USER-E2E-029` TC-GS-USER-144 langkah 5, `TC-GS-USER-E2E-035` TC-GS-USER-192 langkah 60, dan setiap spec lain yang meminta verifikasi "tombol menampilkan state hover".
- **Spec meminta:** tombol [Submit]/[Save] menampilkan state hover.
- **Kenyataannya:** gaya hover Button ditentukan preset Wangs UI dan tidak membawa state yang bisa dibaca (bukan perilaku).
- **Karena:** detail visual milik preset komponen, sama dengan CD-012 (CD-032).
- **Keputusan:** langkah hover tidak diasersi; hover tetap dilakukan bila langkah berikutnya bergantung padanya.
- **Diputuskan oleh:** sesi Integration bersama Wangs-UI Coordinator (CD-032), 2026-11-05.
- **Diterapkan di:** skrip User 029 dan 035, ditandai `// @spec-decision: D-092`.

## D-093 Delete Brand yang sudah dihapus admin lain mengikuti kontrak: 200 dengan baris `deleted`, bukan 404 (2026-11-05)

- **Spec / langkah:** `TC-GS-BRAND-E2E-026` TC-GS-BRAND-103 langkah 6.
- **Spec meminta:** respons Delete untuk Brand yang sudah dihapus admin lain berstatus `404`.
- **Kenyataannya:** kontrak (`global-settings/brand/API/openapi.yaml` L175-216) mendefinisikan Delete sebagai operasi per baris tanpa `404`; id yang sudah tidak ada dilaporkan sebagai `deleted` (operasi idempoten), jawaban `200`.
- **Karena:** perilaku backend mengikuti kontrak API, sama dengan D-087.
- **Keputusan:** skrip menegaskan jawaban kontrak (`200`, baris itu `deleted`) dan bahwa Brand tetap tidak ada; langkah lain TC-103 (toast, Changelog satu entri dari admin kedua) tetap seperti spec.
- **Diputuskan oleh:** sesi Integration, 2026-11-05 (kontrak API; tidak menyangkut komponen).
- **Diterapkan di:** skrip Brand 026, ditandai `// @spec-decision: D-093`.

## D-094 Search tidak mencocokkan placeholder nilai kosong `—` (2026-11-05)

- **Spec / langkah:** `TC-GS-FILEMGR-E2E-045` langkah 29-30, dan setiap spec lain yang mencari teks `—` untuk menemukan baris bernilai kosong.
- **Spec meminta:** Search `—` memuat seluruh entri yang New Value-nya kosong.
- **PRD:** `—` adalah tampilan sel untuk nilai kosong (`prd-conventions.md`, kolom "Nilai Kosong"; error-handling §8 null rendering), bukan data tersimpan; Search mencari substring pada nilai kolom yang tersimpan.
- **Karena:** §4 `spec-conflicts`: mencocokkan placeholder tampilan dengan nilai null adalah perilaku baru per kolom di backend tanpa dasar PRD; baris kosong sudah bisa ditemukan lewat Filter dan Sort (nilai kosong di awal/akhir).
- **Keputusan:** langkah 29-30 ditolak: skrip menegaskan Search `—` memberi hasil kosong ("No results found") karena tidak ada nilai tersimpan `—`.
- **Diputuskan oleh:** sesi Integration, 2026-11-05.
- **Diterapkan di:** skrip FileManager 045, ditandai `// @spec-decision: D-094`.

## D-095 Token file client lain adalah grant; isolasi diuji dengan token client ini (2026-11-05)

- **Spec / langkah:** `TC-GS-FILEMGR-E2E-071` TC-GS-FILEMGR-252 langkah 33-37.
- **Spec meminta:** request baca/unduh memakai token terenkripsi yang memuat ID file client lain dijawab 404 `File not found`, identik dengan token file yang tidak pernah ada.
- **Kontrak:** `GET /v2/file-manager/files/{token}` (`global-settings/file-manager/API/openapi.yaml` L210-216, `security: []`): token terenkripsi adalah grant, memuat client id dan file id, dan route membaca file bila file itu ada di client token tersebut; tanpa pengecekan izin.
- **Karena:** token asli milik client lain memuat client id client lain, jadi jawabannya 200 sesuai kontrak (run 2026-11-04: 200, 1024 byte). Isolasi yang dimaksud TC-252 adalah token yang memuat client id client ini dengan file id client lain: file itu tidak ada di client token, jadi jawabannya 404.
- **Keputusan:** langkah 33 memakai token dengan client id client ini dan file id `outsider-photo-{runId}-071.jpg`. Token asli client lain tidak diuji di e2e. Langkah 34 (token file yang tidak pernah ada) dijalankan dan dicek 404 `File not found`. Langkah 33 dan 35-37 menunggu helper yang mencetak token tersebut (`BT-GS-FILEMGR-1`, `@helper-gap`).
- **Diputuskan oleh:** sesi Integration, 2026-11-05.
- **Diterapkan di:** skrip FileManager 071, ditandai `// @spec-decision: D-095`.

## D-096 UI adalah acuan; ekspektasi tampilan yang berbeda dari spec tidak di-assert e2e (2026-11-05)

- **Spec / langkah:** setiap langkah yang skripnya `gaps.check`/`gaps.open` berjenis `ui-gap` atau `component-gap`, dan langkah tampilan murni (tata letak, warna, urutan tombol, bentuk skeleton, fokus setelah aksi, Esc pada confirm Wangs UI). Daftarnya: `plans/_program/ui-expectations-dropped.md` di repo aplikasi.
- **Spec meminta:** tampilan dan perilaku presentasi seperti yang tertulis di spec.
- **Kenyataannya:** banyak tampilan aplikasi sengaja berbeda dari spec demi UI yang lebih baik.
- **Keputusan:** UI yang jadi acuan; spec yang menyesuaikan. Langkah tersebut dilewati (`ui-gap`/`component-gap` tidak dijalankan dan tidak menggagalkan spec) atau dikeluarkan dengan `// @spec-decision: D-096`. Perubahan aplikasi yang dibuat hanya agar sesuai spec dikembalikan (confirm Delete Measurement kembali tertutup oleh Esc; [Clear Field] Measurement tidak memindah fokus; nama field pada pesan custom field Non-Login ditulis apa adanya). Fungsi (data tersimpan, izin, pesan error dari server, alur) tetap di-assert.
- **Batas (user, 2026-11-05):** "UI" berarti tampilan, di luar tampilan data. Tampilan data (format nama seperti `Ahmad F`, tanggal, jam, angka, mata uang, placeholder nilai kosong) tetap mengikuti spec/PRD dan di-assert; bedanya adalah cacat aplikasi (`ui-defect`, menggagalkan spec). Fungsi (data tersimpan atau terbaca dari backend, izin, alur, penanganan jawaban server) juga tetap di-assert sebagai `ui-defect`.
- **Diputuskan oleh:** user, 2026-11-05.
- **Diterapkan di:** `apps/e2e/support/actions/gaps`, skrip GeneralSettings 011, User 003/020/032, Measurement 018/028/033, NonLoginUser 127.

## D-097 Langkah yang butuh hardware TAG dilewati (2026-11-05)

- **Spec / langkah:** setiap langkah yang butuh scan RFID TAG, TAG yang sudah di-pair ke user, atau entri TAG Registry (Pair/Unpair TAG, badge Verified/Unverified, toast hasil scan, sub-bagian User TAG, Audit TAG session). Daftarnya: `plans/_program/hardware-gaps.md` di repo aplikasi.
- **Spec meminta:** scan TAG lewat reader dan hasilnya di UI.
- **Kenyataannya:** scan TAG butuh hardware; cara menjalankannya dari tes belum diketahui, dan scan di UI masih mock (`tagScanMock.ts`).
- **Keputusan:** langkah tersebut ditulis `gaps.check('hardware-gap', …)` / `gaps.open('hardware-gap', …)`: dilewati, dicatat, dan tidak menggagalkan spec, sampai cara menjalankan hardware dan implementasi UI-nya ada.
- **Diputuskan oleh:** user, 2026-11-05.
- **Diterapkan di:** `apps/e2e/support/actions/gaps`; skrip User 018, 024, 041, 042, 050, 057, 061, 068, 071, 074, 138, 139, 142, 147, 153; NonLoginUser 039; ActivityLog 037.

## D-098 Langkah pada fitur yang belum masuk sprint dilewati (2026-11-05)

- **Spec / langkah:** setiap langkah pada fitur yang belum dibangun karena sprint pengerjaannya belum tiba, menurut papan sprint pemilik produk (`plans/_program/sprint-board.md` di repo aplikasi). Contoh: User Detail beserta tab-tabnya (Role, Responsibilities, Non-Login User, Changelog, System Log, User Log) dijadwalkan di Sprint 3 (9–20 Nov 2026), sedangkan suite User, NonLoginUser dan Role sudah menyentuhnya.
- **Spec meminta:** perilaku lengkap fitur itu sesuai PRD.
- **Kenyataannya:** fitur itu belum masuk sprint, jadi belum dibangun atau baru sebagian. Kegagalannya bukan cacat sprint ini.
- **Keputusan:** langkah tersebut ditulis `gaps.check('sprint-gap', …)` / `gaps.open('sprint-gap', …)`, dengan nama fitur dan sprintnya di `where`. Langkah itu dilewati, dicatat, dan spec dihitung lolos atas langkah yang masuk sprint (bukan gagal, bukan blocking). Tag dicabut saat sprint fitur itu dimulai.
- **Diputuskan oleh:** user, 2026-11-05.
- **Diterapkan di:** `apps/e2e/support/actions/gaps`.

## D-099 Navigasi sidebar saat Popup Create Custom Field dirty: popup ditutup dulu (2026-11-07)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-019` TC-GS-UCF-327 langkah 40-47.
- **Spec meminta:** klik menu sidebar Global Settings > Activity Log saat Popup Create dirty terbuka; perpindahan route dicegat dialog `Unsaved Changes` (`[Cancel]` mempertahankan `Umbra`, `[Leave]` membuka Activity Log).
- **Kenyataannya:** DialogForm Create bersifat modal; overlay-nya menutupi sidebar, sehingga klik sidebar tidak dapat terjadi selama popup terbuka.
- **Karena:** perilaku modal komponen (komponen menang atas spec); tidak ada jalur pengguna ke sidebar selama popup terbuka.
- **Keputusan:** popup ditutup dulu: `[✕]` memunculkan dialog `Unsaved Changes` yang sama (`[Cancel]` mempertahankan `Umbra`, `[Leave]` menutup popup), lalu sidebar membuka Activity Log.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-07.
- **Diterapkan di:** skrip CustomFieldUser 019.
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L737-745 (D-draft-C).

## D-100 `Bonus` yang ditempel di Field Name memunculkan `Field name already exists` (2026-11-07)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-016` TC-GS-UCF-59 langkah 41 dan 49.
- **Spec meminta:** langkah 41 Field Name memuat `Bonus ` tanpa emoji; langkah 49 tidak ada pesan error pada Field Name, Dropdown Values, dan Placeholder.
- **Kenyataannya:** `Bonus` adalah field Pre-setup spec yang sama, sehingga Field Name `Bonus ` menampilkan `Field name already exists` (cek keunikan case-insensitive yang diuji spec ini di TC-GS-UCF-56).
- **Karena:** error itu perilaku benar app; langkah 49 bertentangan dengan Pre-setup spec itu sendiri.
- **Keputusan:** langkah 41 hanya memverifikasi isi Field Name (`Bonus `, tanpa emoji); lalu `[Clear Field]` sebelum langkah 42, sehingga langkah 49 membaca field lain tanpa sisa error keunikan.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-07.
- **Diterapkan di:** skrip CustomFieldUser 016.
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L747-755 (D-draft-D).

## D-101 Global Settings tidak terjangkau dari enterprise-management tidak diuji di e2e Client (2026-11-12)

- **Spec / langkah:** AdminConsole/Client `TC-AC-ACC-E2E-049` TC-AC-ACC-507 langkah 16-27; `TC-AC-ACC-E2E-129` TC-AC-ACC-199 langkah 1-9, TC-AC-ACC-214 langkah 21-31, TC-AC-ACC-460 langkah 32-41, TC-AC-ACC-463 langkah 44-56. `TC-AC-ACC-E2E-130` TC-AC-ACC-226 menyebut gangguan yang sama.
- **Spec meminta:** Global Settings dipaksa tidak terjangkau (atau pembuatan Default User di Global Settings gagal) saat Create, Suspend, Bulk Suspend, Unsuspend, dan Bulk Unsuspend Client, lalu operasi gagal seluruhnya tanpa perubahan parsial.
- **Kenyataannya:** gangguan Global Settings dari sisi enterprise-management adalah outage nyata yang tidak dapat dibentuk di stack uji bersama; tidak ada test route untuk itu.
- **Karena:** state yang tidak nyata tidak dibangun lewat route dev; pola yang sama dengan D-021 dan D-026. BT-AC-ACC-12 ditarik.
- **Keputusan:** langkah tersebut keluar dari e2e; perilaku gagal-seluruhnya dijaga unit test backend.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (BT-AC-ACC-12 ditarik).
- **Diterapkan di:** skrip Client 049 dan 129 (`// @spec-decision: pending D-draft-ACC-GS-UNREACHABLE`), Client 130 (catatan pada `@helper-gap:be BT-5`).
- **Sumber:** repo aplikasi `plans/admin-console-client/backend-findings.md` L18; `apps/e2e/specs/AdminConsole/Client/TC-AC-ACC-E2E-049-…/common.test.ts` L83-86, `…/TC-AC-ACC-E2E-129-…/common.test.ts` L47, L109, L122, L135.

## D-102 Nilai default "instalasi baru" Lifecycle Settings tidak diuji di e2e (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingLifecycleSettings `TC-AC-LCS-E2E-011` (TC-AC-LCS-33, 34, 35: Trial Settings, Free Plan Settings, License Timing) dan `TC-AC-LCS-E2E-012` (TC-AC-LCS-36, 37, 38, 39: Client Lifecycle, Recycle Bin, Approval Settings, System Limits), seluruh langkah.
- **Spec meminta:** pada instalasi baru (tab yang belum pernah disimpan, Pre-setup FRESH) tab menampilkan nilai default PRD.
- **Kenyataannya:** Lifecycle Settings adalah satu baris per tab untuk seluruh platform (singleton), dibaca sebagai Principal. Tenant uji baru tidak memiliki baris sendiri, Principal kedua tidak dapat dibuat (`409`), dan kontrak hanya memuat `GET`, `PATCH`, dan `POST …/reset` per tab; tidak ada route yang menghapus baris (BT-AC-LCS-3 tidak dibangun, keputusan Coordinator 2026-11-10).
- **Karena:** keadaan "tab belum pernah disimpan" hanya ada sekali pada backend yang baru dipasang. Nilai default yang sama sudah diverifikasi setelah Reset to Default (TC-AC-LCS-2 sampai 4 dan spec Reset 036, 041, 046, 059, 069, 074, 083).
- **Keputusan:** langkah TC-AC-LCS-33 sampai TC-AC-LCS-39 keluar dari e2e; nilai default diverifikasi lewat Reset to Default.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (di bawah delegasi pemilik 2026-10-31).
- **Diterapkan di:** skrip PlansLicensingLifecycleSettings 011 dan 012 (`// @spec-decision: pending D-draft-LCS-3`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L197-205 (D-draft-LCS-3).

## D-103 Live Preview Setup Column Plans & Features menampilkan baris pertama (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-150` TC-AC-PF-385 langkah 23; `TC-AC-PF-E2E-155` TC-AC-PF-631 langkah 23.
- **Spec meminta:** Live Preview menampilkan data sel yang sama dengan semua baris tabel.
- **Kenyataannya:** Live Preview milik komponen menampilkan baris pertama tabel saja (run PF-s3-3: tabel 4 baris, preview `alpha Tier`; run PF2-s3-8: Default > Archive 4 baris, preview `Plan Arsip Baru`).
- **Karena:** perilaku komponen menang atas spec (aturan pemilik 2026-11-04 dan 2026-11-08).
- **Keputusan:** langkah 23 mengasersi sel baris pertama tabel pada Live Preview.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (di bawah delegasi pemilik 2026-10-31).
- **Diterapkan di:** skrip PlansLicensingPlansFeatures 150 dan 155 (`// @spec-decision: pending D-draft-PF-2`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/integration-findings.md` L144-149 (D-draft-PF-2); `apps/e2e/specs/AdminConsole/PlansLicensingPlansFeatures/TC-AC-PF-E2E-150-…/common.test.ts` L91, `…/TC-AC-PF-E2E-155-…/common.test.ts` L135.

## D-104 Katalog Device Name kosong bukan state nyata; langkahnya keluar dari e2e (2026-11-12)

- **Spec / langkah:** AdminConsole/SettingsDeviceName `TC-AC-DN-E2E-009` TC-AC-DN-25 langkah 1-2, TC-AC-DN-294 langkah 7 dan 9, TC-AC-DN-403 langkah 12-13, TC-AC-DN-449 langkah 20; `TC-AC-DN-E2E-076` TC-AC-DN-216 langkah 28-29.
- **Spec meminta:** Principal tanpa Device Name dan tanpa entri Changelog Device Name (Pre-setup #12 "Principal Tanpa Riwayat"), sehingga list, opsi filter Brand dan Device Name, dan Changelog menampilkan empty state; pada 076, daftar utuh seperti yang dibentuk Pre-setup saja (`Cable Tester` di halaman terakhir Z-A).
- **Kenyataannya:** backend memiliki satu Principal yang dipakai semua suite. Stok Hardware Handheld Reader menjaga Device SKU-nya `in_use`, sehingga Device Name-nya tidak dapat dihapus, dan mengosongkan katalog beserta Changelog-nya merusak seed suite lain (Device Category, Device SKU, Hardware Handheld Reader). Katalog juga memuat baris hidup suite lain (`4-Port Fixed Reader`, `Zebra RFID Reader`).
- **Karena:** katalog Device kosong bukan state nyata lingkungan ini. Aturan pemilik 2026-11-12: state yang tidak dapat dicapai menjadi spec-decision dan ui-client, bukan `helper-gap:be`.
- **Keputusan:** langkah empty state tersebut keluar dari e2e (pindah ke lapisan ui-client); langkah lain spec 009 (tombol `[+ Device Name]`, tanpa load error, dropdown filter yang bukan error, Changelog yang bukan load error atau empty state search, Esc dan tutup) tetap diasersi terhadap katalog bersama. 009 tidak mengosongkan katalog dan tidak lagi berjalan serial.
- **Diputuskan oleh:** pemilik, 2026-11-12 (aturan kelas state tak tercapai); dicatat Wangs-UI Coordinator 2026-11-12.
- **Diterapkan di:** skrip SettingsDeviceName 009 dan 076 (`gaps.check('spec-decision', 'pending D-draft-DN-009-EMPTY-CATALOG …')`).
- **Sumber:** repo aplikasi `plans/admin-console-settings-device/decisions.md` L216 (D-draft-DN-009-EMPTY-CATALOG).

## D-105 Baris Session produk Fixed Asset dihitung di Activity Log Fixed Asset, bukan Global Settings (2026-11-12)

- **Spec / langkah:** Auth/SessionManagement `TC-AUTH-SES-E2E-029` TC-AUTH-SES-93 langkah 15-16; `TC-AUTH-SES-E2E-043` TC-AUTH-SES-141 langkah 16-17.
- **Spec meminta:** jumlah entri `Session ended` untuk Dewi Permata (029) dan Mega Wibowo (043), yang hanya memegang sesi produk Fixed Asset, bertambah 1 di `Global Settings > Activity Log > Session`.
- **Kenyataannya:** scope Global Settings hanya memuat baris platform dan Global Settings; baris Session sesi produk Fixed Asset ada di scope `fixed_asset` (probe slot 2, 2026-11-11; BT-AUTH-SES-14). Langkah 18-19 spec 043 (baris yang sama di Activity Log Fixed Asset) lolos.
- **Karena:** keputusan pemilik 2026-11-09 (BT-GS-ACTLOG-4): setiap produk menyimpan baris Session-nya sendiri.
- **Keputusan:** langkah yang menghitung baris itu di Global Settings > Activity Log > Session keluar dari e2e; baris sesi produk Fixed Asset dihitung di Activity Log Fixed Asset (043 langkah 18-19). 029 juga `native-gap` dan 043 juga `be-bug`; keduanya tetap PI karena itu.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12, atas keputusan pemilik 2026-11-09 (BT-GS-ACTLOG-4).
- **Diterapkan di:** skrip SessionManagement 029 dan 043 (`@spec-decision: pending D-draft-SES-FA-SESSION-LOG`).
- **Sumber:** repo aplikasi `plans/auth/integration-findings.md` L896, L900 (X24-1).

## D-106 SKU adalah field Filter Panel registri All TAGs (2026-11-07)

- **Spec / langkah:** GlobalSettings/AllTags `TC-GS-TAG-E2E-069` TC-GS-TAG-201 langkah 5-7 dan 9.
- **Spec meminta:** daftar field langkah 5 tanpa `SKU`; langkah 9: tidak ada field untuk `SKU` dan `Code`.
- **Kenyataannya:** Filter Panel memuat field `SKU`.
- **PRD:** `global-settings/all-tags/PRD/all-tags.md` L333: SKU Filterable, label `SKU`, multi-select searchable, placeholder `All SKUs`.
- **Karena:** PRD menjadi acuan.
- **Keputusan:** langkah 5-7 memverifikasi field `SKU` (placeholder `All SKUs`) setelah Device Name; langkah 9 hanya memverifikasi tidak ada field `Code`.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-07.
- **Diterapkan di:** skrip AllTags 069 (`@spec-decision: pending`).
- **Sumber:** repo aplikasi `plans/global-settings-tag/integration-findings.md` L48-56.

## D-107 Activate TAG pada entitas Suspended atau Expired ditolak saat sesi dibuka (2026-11-07)

- **Spec / langkah:** GlobalSettings/AllTags `TC-GS-TAG-E2E-012` TC-GS-TAG-319 langkah 6-14 (Suspended dan Expired).
- **Spec meminta:** halaman Activate TAG terbuka; IMEI ditambahkan dan Submit; toast `Changes can't be saved while this workspace is suspended or expired.` muncul saat Submit, lalu IMEI tidak ada di registri.
- **Kenyataannya:** `POST /v2/hardware-tagging/tags/activate/session` dijawab `403` saat `Continue`; app menampilkan toast itu dan halaman Activate tidak terbuka (tanpa entri GPS).
- **PRD:** `global-settings/all-tags/PRD/all-tags.md` EC-01 (L1206): seluruh operasi penambahan tag diblokir dan aksi tulis ditolak server (§18.8). Membuka sesi Activate adalah aksi tulis (POST).
- **Karena:** PRD menjadi acuan; `403` saat sesi dibuka benar.
- **Keputusan:** sesudah `Continue`, langkah memverifikasi toast suspended tampil dan halaman Activate tidak terbuka (tanpa `#gps-input-group`), untuk Suspended dan Expired. Langkah 15-21a (Delete) tetap `@helper-gap` BT-GS-TAG-1.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-07.
- **Diterapkan di:** skrip AllTags 012 (`@spec-decision: pending`).
- **Sumber:** repo aplikasi `plans/global-settings-tag/integration-findings.md` L68-76.

## D-108 Skills memegang satu nilai; multi-value bukan tipe Custom Field (2026-11-09)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-031` TC-GS-USER-156 langkah 33, 37-38; `TC-GS-USER-E2E-040` TC-GS-USER-216 langkah 41, 45. Pre-setup No. 24 menyebut Skills `Multi-Dropdown` (juga di 020, 024, 060, 072, 075, 108, 112, 151, 170, 174).
- **Spec meminta:** pilih Skills `Excel` dan `SQL {runId}`, hapus opsi `SQL {runId}` lewat API, lalu setelah Submit/Save chip `SQL {runId}` hilang dan chip `Excel` tetap.
- **Kenyataannya:** PRD custom-field-user FLD-02 hanya punya enam Data Type (Text, Text Area, Dropdown, Date, Numeric, Phone), sama dengan enum `DataType` di kontrak; iam menolak `multi_dropdown` dengan `422`. Skills di-seed sebagai `dropdown`.
- **Karena:** tipe multi-value tidak ada di PRD maupun API; langkah yang memilih dua nilai adalah cacat spec.
- **Keputusan:** Skills memegang satu nilai. Langkahnya memilih `SQL {runId}` saja, menghapus opsi itu, lalu mengasersi error inline `SQL {runId} no longer exists. Please select another.` dan field Skills kosong. Langkah chip `Excel` tidak berlaku.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-09.
- **Diterapkan di:** skrip User 031 dan 040 (`@spec-decision: pending (draft D-draft-USER-1 …)`); fixture `user.json` (Skills `dropdown`).
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L1456-1464 (D-draft-USER-1).

## D-109 Empty state Activity Log Admin Console dari respons 0 baris pindah ke ui-client (2026-11-12)

- **Spec / langkah:** AdminConsole/ActivityLog `TC-AC-ACAL-E2E-003` TC-AC-ACAL-05 langkah 1-5 (Tab Session) dan TC-AC-ACAL-06 langkah 6-10 (Tab User Action).
- **Spec meminta:** empty state genuinely kosong di kedua tab, dibentuk lewat intercept List dengan respons 0 baris (TC-06 juga mengizinkan entitas baru tanpa aksi).
- **Kenyataannya:** sesi aktor sendiri selalu tercatat, jadi Tab Session tidak pernah kosong di browser yang login. Principal kedua tidak dapat dibuat (`POST /v2/enterprise-management/dev/clients` dengan `isPrincipal: true` dijawab `409 Client already exists`), jadi Tab User Action Principal bersama tidak pernah nol baris. BT-AC-ACAL-7 ditarik.
- **Karena:** keduanya bukan state nyata di stack uji bersama; jawaban bisnis lewat intercept adalah lapisan ui-client (aturan pemilik 2026-11-12).
- **Keputusan:** kedua blok keluar dari e2e dan diuji di lapisan ui-client.
- **Diputuskan oleh:** pemilik, 2026-11-12.
- **Diterapkan di:** skrip ActivityLog 003 (`// @spec-decision: pending D-draft-ACAL-05-ui-client`).
- **Sumber:** repo aplikasi `plans/admin-console-activity-log/backend-findings.md` L14 (BT-AC-ACAL-7); `apps/e2e/specs/AdminConsole/ActivityLog/TC-AC-ACAL-E2E-003-…/common.test.ts` L13-16, L32-35.

## D-110 Nama sheet XLSX Download Activity Log adalah `Sheet1` (2026-11-12)

- **Spec / langkah:** AdminConsole/ActivityLog `TC-AC-ACAL-E2E-039` TC-AC-ACAL-123 langkah 27.
- **Spec meminta:** nama sheet berkas `Activity-Log-User-Action`.
- **Kenyataannya:** XLSX adalah berkas backend; berkasnya memiliki sheet `["Sheet1"]`.
- **Karena:** Export Contract v1 (`plans/_program/prd-overrides.md` baris 12, pemilik 2026-11-11, be-core-utils #29) menetapkan sheet `Sheet1`, dan backend sesuai kontrak; literal spec sudah usang.
- **Keputusan:** langkah 27 mengasersi nama sheet `Sheet1`.
- **Diputuskan oleh:** pemilik, 2026-11-11 (Export Contract v1); dicatat Wangs-UI Coordinator 2026-11-12.
- **Diterapkan di:** skrip ActivityLog 039 (`gaps.check('spec-decision', 'pending D-draft-ACAL-SHEET-NAME …')`).
- **Sumber:** repo aplikasi `plans/admin-console-activity-log/integration-findings.md` L53.

## D-111 Drag-select teks tautan nama adalah perilaku browser, keluar dari e2e (2026-11-11)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-007` TC-AC-CS-566 langkah 32-34. Keputusan yang sama mencakup AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-044` TC-AC-PF-777 langkah 2-10 dan TC-AC-PF-779 langkah 17-19 (D-draft-ACPF-3).
- **Spec meminta:** tekan-geser-lepas di atas nama Client (atau Plan Name) menyeleksi teksnya dan tidak menavigasi; pada TC-AC-PF-777 Ctrl+klik dan klik tengah membuka tab baru.
- **Kenyataannya:** itu perilaku browser sendiri untuk anchor; app tidak menambah logika. TestSpectra tidak memiliki tekan-geser-lepas.
- **Karena:** perilaku native browser, bukan perilaku app.
- **Keputusan:** langkah tersebut keluar dari e2e. Target tautan (href), yang dimiliki app, tetap diasersi di tempat spec membacanya.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-11.
- **Diterapkan di:** skrip LicenseAllocationSubscription 007 (`// @spec-decision: pending D-draft-ACCS-04`, menggantikan `wrapper-gap`) dan PlansLicensingPlansFeatures 044 (`// @spec-decision: D-draft-ACPF-3`).
- **Sumber:** repo aplikasi `plans/admin-console-license-allocation-subscription/decisions.md` L325-332 (D-draft-ACCS-04); `plans/admin-console-plans-licensing/decisions.md` L282-289 (D-draft-ACPF-3).

## D-112 (ditarik oleh D-175) CS 074 menjalankan blok cancel-while-Waiting-for-Approval pada request trial tanpa harga (2026-11-12)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-074` TC-AC-CS-282 langkah 1-11, TC-AC-CS-615 langkah 12-25, TC-AC-CS-210 langkah 26-30, TC-AC-CS-286 langkah 31-32.
- **Spec meminta:** request berbayar Partner Rina (Plan Owner CV Karya Mandiri, Start Date 19/08/26).
- **Kenyataannya:** request berbayar tidak dapat dibuat selama pricing di luar semua sprint (papan sprint c5f74ebb2; `POST /subscriptions` dijawab `409 Price not set`). Request trial FAMS Professional aktor Create-Only Fajar (30 hari, asset 50, user 10) tidak butuh harga dan melewati perilaku cancel-while-Waiting-for-Approval yang sama.
- **Karena:** pricing belum masuk sprint.
- **Keputusan:** langkah dijalankan pada request trial pengganti; Plan Owner (Principal) dan Start Date (hari ini) diasersi dengan nilai pengganti itu. Hanya cabang renew yang ditolak pada TC-AC-CS-216 tetap `sprint-gap` pricing. Saat pricing masuk sprint, langkah kembali ke request berbayar Rina.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12.
- **Diterapkan di:** skrip LicenseAllocationSubscription 074 (`pending D-draft-CS-074-PRICE-FREE-STANDIN`).
- **Sumber:** repo aplikasi `plans/admin-console-license-allocation-subscription/decisions.md` L379-386.

## D-113 Plan Custom yang di-archive saat dipegang term Active tidak diuji di e2e (2026-11-11)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-144` TC-AC-CS-539 langkah 21-26 dan 30.
- **Spec meminta:** state "plan Custom `Maju Custom` di-archive saat term FAMS Active memegangnya", lalu term dan baris List tidak berubah.
- **Kenyataannya:** produk tidak dapat mencapai state itu. PRD Plans & Features memblokirnya dengan dialog `Cannot Archive Plan`, dan backend menjawab `POST /v2/enterprise-management/plans-features/{planId}/archive` dengan `409 This plan is currently assigned to one or more clients` (slot 2, 2026-11-11). Membentuknya lewat route dev menguji state yang tidak dapat dibuat pengguna.
- **Karena:** state tidak nyata.
- **Keputusan:** langkah tersebut keluar dari e2e; guard `409` dijaga unit test backend. Spec ini tidak mengasersi `409` (itu perilaku spec PF Cannot Archive).
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-11 (lembar keputusan pemilik).
- **Diterapkan di:** skrip LicenseAllocationSubscription 144 (`gaps.check('spec-decision', 'pending D-draft-CS-ARCHIVED-PLAN-HELD …')`).
- **Sumber:** repo aplikasi `plans/admin-console-license-allocation-subscription/decisions.md` L354-361; `integration-findings.md` L208.

## D-114 Push Update oleh Principal Update-Only tidak dapat dicapai (2026-11-11)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-035` TC-AC-PF-88 langkah 22-27 (Overlay Row Action `PT Push Satu` > `Push Update` > `[Push Update]` > toast sukses > Plan Version terbaru tanpa `Outdated`).
- **Spec meminta:** Principal Update-Only (Manage plans & licensing Read + Update) mem-push pembaruan plan ke client eligible.
- **Kenyataannya:** Push Update butuh Manage active client Update pada baris client (PRD §4.1.3 ACPF-LOGIC-09; LLD `plan-list.md` L1312). Flag baris itu by design (dikonfirmasi BE), bukan temuan BE. Persona tidak memegang role Manage active client, jadi menu tidak memuat Push Update (run PF-s3-17).
- **Karena:** PRD menang; cacat spec. Pre-setup tidak diubah (memberi persona Manage active client mengubah Pre-setup spec).
- **Keputusan:** langkah 22-27 keluar dari e2e sampai pemilik spec memindahkan push ke aktor yang memegang Manage active client Update. Langkah 18-21, edit plan (TC-AC-PF-81), dan rename (TC-AC-PF-85) tetap diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-11 (opsi a: PRD §4.1.3 ACPF-LOGIC-09 menang, tanpa perubahan app).
- **Diterapkan di:** skrip PlansLicensingPlansFeatures 035 (`// @spec-decision: pending D-draft-acpf-push-update-needs-manage-active-client`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L242-249.

## D-115 Archive oleh Principal Group-Mix tidak dapat dicapai (2026-11-10)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-040` TC-AC-PF-107 langkah 16-20 (Overlay Row Action `Paket Blok Mask` > `Archive` > dialog `Cannot Archive Plan` > `[OK]`).
- **Spec meminta:** Principal Group-Mix (Pre-setup #8) mengklik `Archive` pada `Paket Blok Mask` dan membaca dialog `Cannot Archive Plan`.
- **Kenyataannya:** Archive butuh hak Delete Manage plans & licensing; Pre-setup #8 hanya memegang Read + Update, sehingga `Archive` tersembunyi untuk aktor itu dan langkah 17-20 tidak dapat dicapai. Notes spec sendiri menandai konflik ini (prasyarat TC-AC-PF-107 "aktor memiliki Delete").
- **Karena:** cacat spec; Pre-setup #8 tidak diubah.
- **Keputusan:** langkah 16-20 keluar dari e2e; aktor tidak diganti.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (Pre-setup tidak diubah), dicatat 2026-11-12.
- **Diterapkan di:** skrip PlansLicensingPlansFeatures 040 (`// @spec-decision: pending D-draft-ACPF-1`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L233-240.

## D-116 Memilih Product pada form New Custom Plan adalah perubahan form (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-063` TC-AC-PF-160 langkah 16-19.
- **Spec meminta:** setelah `[Clear Field]`, memilih Product `FAMS` lalu keluar lewat breadcrumb dianggap form identik (tanpa dialog `Unsaved Changes`).
- **Kenyataannya:** form New Custom Plan dimulai tanpa Product (placeholder `Select product`, `Product must not be empty`); memilih `FAMS` adalah perubahan dari keadaan awal, jadi guard form menanyakan `Unsaved Changes` (run PF-s3-2: dialog terbuka di `/new-custom`).
- **Karena:** perilaku guard form benar; cacat spec.
- **Keputusan:** skrip mengonfirmasi `[Leave]` lalu melanjutkan; langkah 19 "tanpa dialog" tidak diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (di bawah delegasi pemilik 2026-10-31).
- **Diterapkan di:** skrip PlansLicensingPlansFeatures 063 (`// @spec-decision: pending D-draft-PF-1`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/integration-findings.md` L137-142 (D-draft-PF-1).

## D-117 Changelog Group yang benar-benar kosong bukan state nyata; langkahnya pindah ke ui-client (2026-11-12)

- **Spec / langkah:** AdminConsole/SettingsGroup `TC-AC-SG-E2E-067` TC-AC-SG-242 langkah 30, Pre-setup #43 (`Distributor Changelog Kosong`).
- **Spec meminta:** modal Changelog: Group milik entitas tanpa entri Group menampilkan empty state genuinely empty (`No changelog yet`, `Activities and changes will appear here.`).
- **Kenyataannya:** Distributor tidak dapat dibuat di stack ini (BT-21), jadi entitasnya berdiri di Principal bersama. Changelog Group-nya memuat baris Group dari setiap suite yang membuat, mengganti nama, atau menghapus group di sana (Role & Permission, Settings User, Client, Plans & Features, Subscription).
- **Karena:** Changelog Group yang kosong bukan state lingkungan ini. Aturan pemilik 2026-11-12: state yang tidak dapat dicapai menjadi spec-decision dan ui-client.
- **Keputusan:** langkah 30 keluar dari e2e (pindah ke lapisan ui-client). Langkah 27-29 dan 31 tetap berjalan; langkah modal Changelog lain di 067-071 dan 114 membaca seed run ini saja.
- **Diputuskan oleh:** pemilik, 2026-11-12 (aturan kelas state tak tercapai); dicatat Wangs-UI Coordinator 2026-11-12.
- **Diterapkan di:** skrip SettingsGroup 067 (`gaps.check('spec-decision', 'pending D-draft-SG-067-EMPTY-CHANGELOG …')`).
- **Sumber:** repo aplikasi `plans/admin-console-settings-group/decisions.md` L316-322.

## D-118 Download Version History gagal dipicu dengan 5xx, bukan 422 (2026-11-12)

- **Spec / langkah:** AdminConsole/SettingsPrivacyPolicy `TC-AC-PP-E2E-007` TC-AC-PP-141 langkah 26.
- **Spec meminta:** respons Download (export) dipaksa `422` lewat intercept.
- **Kenyataannya:** berkas dibangun di server (`POST …/versions/export`, Export Contract v1); tidak ada input atau state nyata yang membuat export menjawab `422`. PRD V-03 / T-03 memberi satu teks untuk setiap kegagalan Download selain penolakan EC-28.
- **Karena:** `422` di sini adalah injeksi kegagalan; transport fault `5xx` melewati jalur UI yang sama, dan aturan `422` dijaga uji backend.
- **Keputusan:** langkah 26 memasang intercept `500` pada `…/versions/export`; toast error persisten `Error, failed to download Privacy-Policy-Version-History.` tetap diasersi (langkah 27-31).
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (di bawah delegasi pemilik 2026-10-31).
- **Diterapkan di:** skrip SettingsPrivacyPolicy 007 (`// @spec-decision: pending D-draft-PP-141-fault-5xx`).
- **Sumber:** repo aplikasi `apps/e2e/specs/AdminConsole/SettingsPrivacyPolicy/TC-AC-PP-E2E-007-resilience-baca-tabel-dan-export/common.test.ts` L118-128; `plans/admin-console-settings-privacy-policy/integration-findings.md` L88.

## D-119 Aktor tanpa `manage_privacy_policy` tidak memiliki grup Settings (2026-11-10)

- **Spec / langkah:** AdminConsole/SettingsUser `TC-AC-SU-E2E-016` TC-AC-SU-52 langkah 27-28 (Group Manager saja, `Dedi Kurnia`) dan 36-37 (Manage TAG stock saja, `Rudi Hartono`).
- **Spec meminta:** kedua aktor membuka grup Settings di sidebar dan melihat `Privacy Policy` tanpa `User`.
- **Kenyataannya:** aktor tanpa `manage_privacy_policy` tidak memiliki grup Settings sama sekali (core `routeAccess`, F-INT-SU-3), jadi anchor `Privacy Policy` tidak ada.
- **Karena:** gerbang menu app; langkah anchor tidak dapat dicapai.
- **Keputusan:** langkah anchor (buka grup Settings, `Privacy Policy` tampil) keluar dari e2e; ketiadaan `User` tetap diasersi tanpa anchor itu.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (draf disetujui), dicatat 2026-11-12.
- **Diterapkan di:** skrip SettingsUser 016 (`pending D-draft-SU-016-PP`).
- **Sumber:** repo aplikasi `plans/admin-console-settings-user/decisions.md` L139.

## D-120 Division login user tidak bisa kosong (2026-11-09)

- **Spec / langkah:** Auth/LoginPassword `TC-AUTH-LP-E2E-039` TC-AUTH-LP-127 prasyarat (Winarsih Kusuma tanpa Employee ID, Position, dan Division) dan langkah 22 (Division "—").
- **Spec meminta:** baris login Winarsih di `Global Settings > Activity Log > Session` menampilkan Employee ID "—", Position "—", dan Division "—".
- **Kenyataannya:** Division wajib untuk login user: PRD `global-settings/user` §9.9 Validation Rules ("Division *"), V-09 "Division must not be empty"; kontrak create user mewajibkan `divisionId`; Division yang dipakai tidak bisa dihapus. Login user tanpa Division tidak dapat dicapai lewat produk.
- **Karena:** PRD menang atas spec; cacat spec.
- **Keputusan:** TC-AUTH-LP-127 hanya memverifikasi Employee ID "—" dan Position "—" (Winarsih dibuat tanpa keduanya); bagian Division dari langkah 22 keluar dari e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-09.
- **Diterapkan di:** skrip LoginPassword 039 TC-AUTH-LP-127 langkah 22 (`// @spec-decision: pending D-draft-AUTH-2`).
- **Sumber:** repo aplikasi `plans/auth/integration-findings.md` L861-869 (D-draft-AUTH-2).

## D-121 Symbol wajib di Column Mapping Import Measurement (2026-11-11)

- **Spec / langkah:** GlobalSettings/Import `TC-GS-IMPORT-E2E-014` TC-GS-IMPORT-887 langkah 14 dan TC-GS-IMPORT-886 langkah 77.
- **Spec meminta:** Symbol opsional: tidak ada Error Banner (langkah 14) dan Error Banner tidak memuat `Symbol` (langkah 77) saat Symbol tetap "No Column".
- **Kenyataannya:** TC-GS-IMPORT-56 (spec 015) dan app memperlakukan Symbol sebagai wajib; dengan Symbol pada "No Column" Error Banner sebelum Confirm mencantumkannya (run ImpCs-B3-20261112-0029: banner memuat "Unit Name" dan "Symbol").
- **Karena:** spec bertentangan dengan TC-GS-IMPORT-56 dan app; catatan "Symbol opsional" pada 887 adalah cacat spec.
- **Keputusan:** langkah mengasersi Error Banner yang mencantumkan Symbol.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-11.
- **Diterapkan di:** skrip Import 014 (`pending D-draft-IMP-SYMBOL-REQUIRED`).
- **Sumber:** repo aplikasi `plans/global-settings-import/decisions.md` L320-326.

## D-122 Baris 5 ke bawah template User Login tanpa styling terlihat; format Text diizinkan (2026-11-12)

- **Spec / langkah:** GlobalSettings/Import `TC-GS-IMPORT-E2E-168` TC-GS-IMPORT-451 langkah 16, 20, dan 23.
- **Spec meminta:** langkah 23 "baris 5 ke bawah kosong tanpa styling"; langkah 16 dan 20 sel Employee ID, Active Period, dan Emergency Phone pada baris 5 berformat Text.
- **Kenyataannya:** spec bertentangan dengan dirinya sendiri: format Text pada baris 5 adalah styling baris 5.
- **Karena:** kedua langkah tidak dapat benar bersamaan.
- **Keputusan:** baris 5 ke bawah tidak memuat nilai dan tanpa styling terlihat (tanpa fill, bold, warna font, wrap); format angka Text pada selnya (langkah 16 dan 20) diizinkan, seperti yang ditulis template backend. Langkah 23 diasersi dengan cara itu; langkah 19 dan 20 tetap seperti tertulis.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12.
- **Diterapkan di:** skrip Import 168 langkah 23 (`pending D-draft-IMP-TEMPLATE-ROW5-STYLE`). 168 juga `library-gap`.
- **Sumber:** repo aplikasi `plans/global-settings-import/decisions.md` L328-335.

## D-123 Search `fajar n` di Modal Changelog User saat Modified By di-hide (2026-11-12)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-078` TC-GS-USER-475 langkah 70.
- **Spec meminta:** Search `fajar n` dengan kolom Modified By di-hide menampilkan `No results found`.
- **Kenyataannya:** `fajar n` juga cocok dengan User Name yang tampil `Fajar Nugroho` (entri Create dan Role Pre-setup No. 4 miliknya sendiri), jadi tabel tidak kosong (run GSUR-C-3).
- **Karena:** cacat spec: kata kunci cocok dengan kolom lain yang tampil.
- **Keputusan:** langkah mengasersi bahwa kolom tersembunyi tidak dicari: tidak ada baris selain milik Fajar Nugroho, dan baris Create Beta (yang cocok hanya lewat Modified By `Fajar N`) tidak tampil; setelah unhide baris itu tampil.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (di bawah delegasi pemilik 2026-10-31).
- **Diterapkan di:** skrip User 078 (`@spec-decision: pending D-draft-USER-2`). 078 juga `be-bug`.
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L1492-1498 (D-draft-USER-2).

## D-124 Search `Create` di Modal Changelog User juga mencocokkan Field `Create` (2026-11-12)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-083` TC-GS-USER-505 langkah 20.
- **Spec meminta:** setelah Search `Create`, setiap baris berkas unduhan ber-Action `Create`.
- **Kenyataannya:** Search mencocokkan semua kolom yang tampil; baris System Role (Action `Edit`, User Name `Manage user and role — Fajar Nugroho`, Field `Create`) ikut cocok (run GSUR-C-5: kolom Action berkas `["Edit","Edit","Edit"]` di samping baris Create).
- **Karena:** cacat spec.
- **Keputusan:** langkah mengasersi bahwa setiap baris memuat `create` di salah satu kolom yang dicari, bukan bahwa Action-nya `Create`.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-12 (di bawah delegasi pemilik 2026-10-31).
- **Diterapkan di:** skrip User 083 (`@spec-decision: pending D-draft-USER-3`).
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L1588-1594 (D-draft-USER-3).

## D-125 Foto user yang dicabut lewat admin override File Manager: Old Value nama berkas, New Value `—` (2026-11-11)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-139` TC-GS-USER-918 langkah 83.
- **Spec meminta:** baris Changelog Detail Action `Edit`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Siti N`.
- **PRD:** `global-settings/user` user.md L1580: pencabutan foto tercatat dengan Old Value nama berkas dan New Value `—`.
- **Karena:** PRD menang atas spec.
- **Keputusan:** satu baris Edit/Photo diasersi; nilai Old/New `—`/`—` dari spec tidak diasersi (BT-GS-USER-16). 139 juga `feature-gap:be` dan `hardware-gap`.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-11.
- **Diterapkan di:** skrip User 139 (`gaps.check('spec-decision', 'pending D-draft-gs-user-photo-fm-removal …')`).
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L1837; `apps/e2e/specs/GlobalSettings/User/TC-GS-USER-E2E-139-…/common.test.ts` L335-338.

## D-126 Principal kedua tidak dapat dibuat: blok Device SKU per plan dan Principal Tanpa SKU keluar dari e2e (2026-11-10)

- **Spec / langkah:** AdminConsole/SettingsDeviceSku `TC-AC-DS-E2E-182` TC-AC-DS-559 langkah 1-13 (Pre-setup #41); `TC-AC-DS-E2E-095` TC-AC-DS-593 langkah 22-27 (Pre-setup #21).
- **Spec meminta:** empat Principal, masing-masing pada plan Starter, Growth, Professional, dan Enterprise (182); Total Control Principal Tanpa SKU dengan dropdown filter Brand dan Device Name `No options available` (095).
- **Kenyataannya:** EMS mengizinkan satu Principal; Principal kedua dijawab `409`, sehingga state itu tidak dapat ada.
- **Karena:** cacat spec; state tidak nyata, bukan helper gap.
- **Keputusan:** blok tersebut keluar dari e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (dari BE), dicatat 2026-11-12.
- **Diterapkan di:** skrip SettingsDeviceSku 182 dan 095 (`gaps.check('spec-decision', 'pending D-draft-DS-PRINCIPALS …')`).
- **Sumber:** repo aplikasi `plans/admin-console-settings-device/decisions.md` L215.

## D-127 Publish Privacy Policy tanpa idempotency key (2026-11-10)

- **Spec / langkah:** AdminConsole/SettingsPrivacyPolicy `TC-AC-PP-E2E-030` TC-AC-PP-91 langkah 15, 17-18 dan TC-AC-PP-206 langkah 68-70; `TC-AC-PP-E2E-031` TC-AC-PP-92 langkah 8-22, TC-AC-PP-93 langkah 28-62, TC-AC-PP-202 langkah 63-80; `TC-AC-PP-E2E-032` TC-AC-PP-94 langkah 7-22, TC-AC-PP-212 langkah 31-39.
- **Spec meminta:** idempotency key pada Publish, replay jawaban pertama, `409` untuk key yang dipakai ulang (dialog D-03), dan masa berlaku key 24 jam.
- **PRD:** Publish tanpa idempotency key (ACPP-LOGIC-07d/07e, LLD L260); timeout 30 detik ada di sisi klien (PRD L496); masa berlaku key tidak ada di PRD, LLD, maupun OpenAPI.
- **Karena:** PRD menjadi acuan. BT-GAP-15 ditarik.
- **Keputusan:** pengiriman ulang adalah request baru; langkah yang butuh key, replay, atau `409` keluar dari e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (draf disetujui, PRD = acuan).
- **Diterapkan di:** skrip SettingsPrivacyPolicy 030, 031, 032 (`gaps.check('spec-decision', 'pending D-draft-PP-IDEMP …')` atau komentar `// @spec-decision`).
- **Sumber:** repo aplikasi `plans/admin-console-settings-privacy-policy/decisions.md` L102.

## D-128 Download Privacy Policy di atas 5.000 baris tidak dijalankan di e2e (2026-11-10)

- **Spec / langkah:** AdminConsole/SettingsPrivacyPolicy `TC-AC-PP-E2E-047` TC-AC-PP-207 langkah 1-10.
- **Spec meminta:** Download lebih dari 5.000 baris (Riwayat D, 5.001 versi) diproses sinkron dan seluruh baris ada pada berkas.
- **Kenyataannya:** PRD sejalan dengan spec (sinkron; LLD L369/L653). Spec di luar filter (Medium, Edge), dan seed 5.001 versinya tidak dapat ditulis (gateway `429`, BT-AC-PP-2).
- **Karena:** seed volume tidak dapat dibentuk di stack uji; BT-GAP-14 ditarik.
- **Keputusan:** spec 047 dilewati di e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (draf disetujui, PRD = acuan).
- **Diterapkan di:** skrip SettingsPrivacyPolicy 047 (`pending D-draft-PP-EXPORT`).
- **Sumber:** repo aplikasi `plans/admin-console-settings-privacy-policy/decisions.md` L104.

## D-129 Baris Failed penolakan Jalur A di Event Log Activate tidak memuat Device Name (2026-11-10)

- **Spec / langkah:** GlobalSettings/HardwareHandheldReader `TC-GS-HHR-E2E-013` TC-GS-HHR-448/449 langkah 17-36, khususnya langkah 25 dan 34.
- **Spec meminta:** baris `Failed` Event Log Activation untuk penolakan Jalur A menampilkan Device Name `Zebra RFID Reader (SKU-HHR-01)`.
- **Kenyataannya:** body Jalur A (`{"rangeType":"Long Range","serialNumber":"SN-HHR-00201","readerPower":31}` atau `aliasName` 121 karakter) tidak memuat `deviceNameId` maupun `skuId`. LLD menjalankan validasi struktur sebelum mencari unit (L326) dan menulis `deviceName` null bila tidak ada yang dipilih (L398); run hhr-s2-r3 menunjukkan `deviceName: null`.
- **Karena:** LLD menjadi acuan; BT-GAP-09 ditarik.
- **Keputusan:** Device Name pada baris tersebut tidak diasersi; kolom lain baris itu (Range Type, PIC) tetap seperti spec.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (draf disetujui).
- **Diterapkan di:** skrip HardwareHandheldReader 013 (`pending D-draft-HHR-LOGNAME`).
- **Sumber:** repo aplikasi `plans/global-settings-hardware/decisions.md` L125; `plans/global-settings-hardware/integration-findings.md` L113.

## D-130 Format tanggal `MM/dd/yyyy` tidak ada di General Settings (2026-11-10)

- **Spec / langkah:** GlobalSettings/HardwareHandheldReader `TC-GS-HHR-E2E-071` blok TC-GS-HHR-392, 393, 394, 395 (format `MM/dd/yyyy` 12-hour).
- **Spec meminta:** General Settings Client A diatur ke `MM/dd/yyyy` 12-hour, lalu list, filter, dan log tampil dalam format itu.
- **Kenyataannya:** enum `dateFormat` OpenAPI general-settings (L283) dan LLD (L88) tidak memuat `MM/dd/yyyy`; `PUT …/general-settings` menjawab `422 Invalid date format` (F-INT-HHR-21/45), sesuai kontrak.
- **Karena:** format spec tidak ada; BT-GAP-10 ditarik.
- **Keputusan:** blok tersebut keluar dari e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-10 (draf disetujui).
- **Diterapkan di:** skrip HardwareHandheldReader 071 (`pending D-draft-HHR-DATEFMT`).
- **Sumber:** repo aplikasi `plans/global-settings-hardware/decisions.md` L124.

## D-131 Item Allocation lain untuk aktor tanpa Manage allocation tidak ada (2026-11-12)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-016` TC-AC-CS-71 langkah 10-11.
- **Spec meminta:** aktor tanpa Manage allocation membuka menu `Allocation` dan sedikitnya satu item Allocation lain tampil, sedangkan `Client Subscription` tidak.
- **Kenyataannya:** gerbang menu membuka Device Allocation, License Allocation dan Client Subscription dengan satu aturan (Read pada Group Role `manage_allocation`, atau Group Manager sebuah group). Aktor yang melihat salah satunya juga melihat Client Subscription; memberi Group Role mematahkan langkah 12.
- **Karena:** keadaan awal langkah 10-11 tidak ada di matriks akses menu.
- **Keputusan:** langkah 10-11 keluar dari e2e; aktor tidak diganti. Langkah 12 dan seterusnya tetap seperti spec.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12.
- **Diterapkan di:** skrip LicenseAllocationSubscription 016 (`pending D-draft-ACCS-05`).
- **Sumber:** repo aplikasi `plans/admin-console-license-allocation-subscription/integration-findings.md` L125-133; `plans/access/ac-menu-access-matrix.md` baris 5-7.

## D-132 Search kolom Modified By yang di-hide memakai kata kunci yang hanya ada di Modified By (2026-11-12)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-071` TC-GS-USER-419 langkah 103.
- **Spec meminta:** Search `System` dengan kolom Modified By di-hide menampilkan `No results found`.
- **Kenyataannya:** `System` juga cocok dengan Email setiap user Pre-setup (`@qwertysystem.net`), kolom yang tampil, jadi tabel tidak akan kosong.
- **Karena:** kata kunci spec tidak menguji maksud langkahnya (kolom yang di-hide tidak ikut dicari).
- **Keputusan:** langkah 103 memakai kata kunci yang hanya ada di Modified By (nama aktor pengubah yang dibuat run), lalu mengasersi `No results found` seperti spec.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12.
- **Diterapkan di:** skrip User 071 (`pending D-draft-USER-5`).
- **Sumber:** repo aplikasi `plans/global-settings-user/integration-findings.md` L1596-1602.

## D-133 Label Time Zone mengikuti daftar `(UTC±HH:MM) City` override owner (2026-11-12)

- **Spec / langkah:** GlobalSettings/GeneralSettings `TC-GS-GSET-E2E-014` TC-GS-GSET-33, `TC-GS-GSET-E2E-040` TC-GS-GSET-163, `TC-GS-GSET-E2E-041` TC-GS-GSET-105.
- **Spec meminta:** label opsi Time Zone dikelompokkan seperti PRD, dan label log untuk `Etc/UTC` mengikuti teks PRD.
- **Kenyataannya:** override owner general-settings 2026-10-19 menetapkan daftar `(UTC±HH:MM) City`; app mengirim `Etc/UTC` dengan label `(UTC+00:00) UTC` dari daftar yang sama.
- **Karena:** override owner berlaku atas PRD untuk daftar ini.
- **Keputusan:** label opsi dan label New/Old Value log diasersi sesuai daftar override (`Etc/UTC` = `(UTC+00:00) UTC`); nilai Asia/Jakarta `(UTC+07:00) Bangkok, Hanoi, Jakarta` tetap diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12, mengikuti override owner 2026-10-19.
- **Diterapkan di:** skrip GeneralSettings 014, 040, 041 (`pending D-draft-gset-timezone-labels`).
- **Sumber:** repo aplikasi `plans/global-settings-general-settings/integration-findings.md` L102; `plans/_program/prd-overrides.md` baris general-settings 2026-10-19.

## D-134 Counter Bulk Action Bar Client mengikuti teks i18n app `N Clients selected` (2026-11-12)

- **Spec / langkah:** AdminConsole/Client `TC-AC-ACC-E2E-306` TC-AC-ACC-448; `TC-AC-ACC-E2E-303` TC-AC-ACC-718, 719, 720.
- **Spec meminta:** counter Bulk Action Bar terbaca `N clients selected`.
- **Kenyataannya:** app menampilkan `N Clients selected` dari string i18n `Strings.ClientSelected` (`# Client selected` / `# Clients selected`) lewat t() dan ICU, ada di setiap locale. Pola PRD client.md L503 `[N] [Item] selected` tidak menetapkan huruf besar-kecil item.
- **Karena:** aturan tim 18 (owner 2026-11-10): teks UI mengikuti i18n app, bukan kata PRD apa adanya.
- **Keputusan:** langkah e2e mengasersi teks app `N Clients selected`.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12.
- **Diterapkan di:** skrip Client 303 dan 306 (`pending D-draft-ACC-COUNTER-COPY`).
- **Sumber:** repo aplikasi, commit ae7fc8991 dan 7bb2e215c (feat/connect-api); PRD admin-console client.md L503.

## D-135 Filter Custom Field User dipasang sebelum Search (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-053` TC-GS-UCF-217.
- **Spec meminta:** Search dulu, lalu filter; hasilnya kosong.
- **Kenyataannya:** opsi filter mengikuti search yang aktif (kontrak custom-field-user L93), jadi setelah search, opsi yang dipakai spec tidak lagi tersedia.
- **Keputusan:** urutan langkah menjadi filter dulu, lalu search. Hasil yang diasersi (kosong) tidak berubah.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12.
- **Diterapkan di:** skrip CustomFieldUser 053 (`pending D-draft-UCF-053-FILTER-ORDER`).
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-UCF-053-FILTER-ORDER); kontrak custom-field-user L93.

## D-136 Batas waktu tepat satu detik di Auth diuji dengan margin di e2e, titik batasnya di unit test backend (2026-11-12)

- **Spec / langkah:** Auth/Mfa 008 (TC-AUTH-MFA-211), 025 (TC-216), 029 (TC-212, 213), 033 (TC-164 langkah 71 dan 82-89), 042 (TC-214), 054 (TC-215); Auth/ResetPassword 021 (TC-AUTH-RST-149), 028 (TC-143 langkah 35-45); Auth/SessionManagement 013 (TC-AUTH-SES-282), 017 (TC-283).
- **Spec meminta:** jam server diset dan dibekukan di satu instan (T0 + N), lalu satu request mendarat tepat di batas (4:59, 9:59, 10:00, 24 jam, 90 hari, 180 hari, 59/60 detik).
- **Kenyataannya:** helper waktu yang ada hanya `POST /v2/iam/dev/time/age` (menggeser kolom waktu tenant, tidak membekukan jam). Jam nyata terus berjalan antara pemanggilan helper dan request browser, jadi baris yang dituakan tepat ke batas sudah lewat saat request tiba (AccountActivation 027 TC-137 menjawab Expired).
- **Karena:** batasnya perbandingan satu detik di backend; run e2e lewat browser tidak bisa menempatkan request di satu detik (alasan yang sama dengan D-021).
- **Keputusan:** e2e mengasersi dua sisi batas dengan margin lewat `ageTime`. Langkah instan-tepat keluar dari e2e: seluruh blok untuk TC yang hanya berisi batas (MFA 025 TC-216, MFA 054 TC-215, RST 021 TC-149, SES 013 TC-282, SES 017 TC-283, MFA 029 TC-212/213, MFA 008 TC-211, MFA 042 TC-214), sebagian untuk MFA 033 TC-164 dan RST 028 TC-143. Sisi inklusif/eksklusif dijaga unit test iam dengan jam yang diinjeksi (iam#115); batas yang belum punya unit test dicatat sebagai baris BT, bukan langkah e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** skrip di atas (`pending D-draft-AUTH-EXACT-INSTANT`).
- **Sumber:** repo aplikasi `plans/auth/decisions.md` L684-702 (branch feat/connect-api-c f42174bed); `plans/_program/backend-test-findings.md` L124 (BT-56); PROJECT.md `## Backend test helpers`.

## D-137 Gangguan layanan geo-IP tidak bisa dibuat; fail-open dijaga unit test backend (2026-11-12)

- **Spec / langkah:** Auth/LoginPassword `TC-AUTH-LP-E2E-028` TC-AUTH-LP-155 langkah 12-22; Auth/Mfa `TC-AUTH-MFA-E2E-026` TC-AUTH-MFA-45 langkah 1-15, TC-AUTH-MFA-46 langkah 25, TC-AUTH-MFA-209 langkah 37-50.
- **Spec meminta:** layanan geo-IP dimatikan dengan failure injection, lalu login dari lokasi jauh tanpa MFA (fail-open).
- **Kenyataannya:** tidak ada route yang membuat lookup geo-IP gagal di stack bersama.
- **Karena:** gangguan layanan pihak ketiga tidak bisa distage di stack bersama (pola yang sama dengan D-021).
- **Keputusan:** langkah gangguan keluar dari e2e; perilaku fail-open dijaga unit test iam. Langkah yang tidak bergantung pada gangguan tetap jalan.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** skrip LoginPassword 028 dan Mfa 026 (`pending D-draft-AUTH-GEOIP-FAILOPEN`).
- **Sumber:** repo aplikasi `plans/auth/decisions.md` L703-715 (feat/connect-api-c f42174bed); BT-35.

## D-138 Penolakan token reCAPTCHA oleh server pindah ke ui-client (2026-11-12)

- **Spec / langkah:** Auth/ResetPassword `TC-AUTH-RST-E2E-038` TC-AUTH-RST-121 langkah 12-15; `TC-AUTH-RST-E2E-043` TC-AUTH-RST-137 langkah 64.
- **Spec meminta:** `POST /v2/iam/auth/reset-password/request` dengan `recaptchaToken: "invalid-token"` ditolak server karena reCAPTCHA.
- **Kenyataannya:** proyek memakai pasangan kunci uji v2 Google; setiap token lolos verifikasi (keputusan owner BT-6, 2026-10-29). Token `invalid-token` tidak ditolak, justru mereset user sungguhan. Kasus tanpa token (TC-120, 124) ditolak server dan sudah dibangun.
- **Karena:** penolakan ini hanya bisa dibuat dengan jawaban tiruan, jadi termasuk ui-client (aturan state yang tidak bisa dicapai, owner 2026-11-12).
- **Keputusan:** langkah tersebut keluar dari ui-e2e; ui-client me-mount unit Reset Password request, menjawab request dengan penolakan reCAPTCHA sesuai kontrak (4xx operasi reset-password/request di openapi auth), dan mengasersi caption serta tidak adanya langkah email. Penolakan verifier sendiri dijaga test backend iam.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** skrip ResetPassword 038 dan 043 (`pending D-draft-AUTH-RECAPTCHA-REJECT`).
- **Sumber:** repo aplikasi `plans/auth/decisions.md` L716-725 (feat/connect-api-c f42174bed); PROJECT.md L184-187; `plans/_program/backend-test-findings.md` L74.

## D-139 Ucapan screen reader di MFA 056 diperiksa manual; e2e mengasersi markup live region (2026-11-12)

- **Spec / langkah:** Auth/Mfa `TC-AUTH-MFA-E2E-056` TC-AUTH-MFA-12 langkah 8, 12, 13, 14.
- **Spec meminta:** screen reader uji dijalankan dan keluarannya dibaca otomatis.
- **Kenyataannya:** tidak ada action atau API TestSpectra yang menjalankan screen reader atau membaca ucapannya; TC sumber menandai TC-AUTH-MFA-12 Manual Only.
- **Karena:** ucapan screen reader adalah keluaran teknologi bantu di OS tertentu; yang dikendalikan app adalah markup-nya.
- **Keputusan:** langkah 8, 12 dan 14 keluar dari run otomatis (cek aksesibilitas manual per rilis). Langkah 13 di e2e mengasersi yang dibuktikan DOM: region error punya `aria-live` assertive atau `role="alert"` saat caption muncul, dan fokus tidak berpindah.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** skrip Mfa 056 (`pending D-draft-AUTH-SCREEN-READER`).
- **Sumber:** repo aplikasi `plans/auth/decisions.md` L726-735 (feat/connect-api-c f42174bed).

## D-140 Request Create Session langsung keluar dari e2e (2026-11-12)

- **Spec / langkah:** Auth/SessionManagement `TC-AUTH-SES-E2E-064` TC-AUTH-SES-235 langkah 1-5, TC-AUTH-SES-320 langkah 6-11, TC-AUTH-SES-250 langkah 12-17; `TC-AUTH-SES-E2E-069` TC-AUTH-SES-320 langkah 1-7, TC-AUTH-SES-250 langkah 8-14.
- **Spec meminta:** request Create Session dengan token user tertentu (platform tidak valid, user Pending Activation, user Active OFF) ditolak tanpa session.
- **Kenyataannya:** kontrak tidak punya operasi Create Session publik; session dibuat di dalam `POST /v2/iam/auth/login`, dan login nyata menolak user Pending Activation dan Active OFF sebelum token ada. Tidak ada route uji yang menerbitkan token untuk user yang ditolak (BT-AUTH-SES-12).
- **Karena:** operasi itu langkah internal login, bukan panggilan publik.
- **Keputusan:** request Create Session langsung keluar dari e2e; penolakannya dijaga test integrasi iam. E2E membuktikan hasil yang terlihat user lewat login nyata di spec LoginPassword yang mencakup penolakan Pending Activation dan Active OFF.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (opsi A usulan Integration C).
- **Diterapkan di:** skrip SessionManagement 064 dan 069 (`pending D-draft-AUTH-CREATE-SESSION`; 069 sebelumnya `feature-gap:be`).
- **Sumber:** repo aplikasi `plans/auth/decisions.md` L736-744 (feat/connect-api-c f42174bed); `plans/auth/backend-findings.md` L22.

## D-141 Kriteria filter yang opsinya hilang tetap jalan sebagai snapshot nilai lama (2026-11-12)

- **Spec / langkah:** GlobalSettings/FileManagerE2 `TC-GS-FILEMGR2-E2E-005` grup 4, langkah 33.
- **Spec meminta:** setelah file satu-satunya milik `Bimo Sementara` dihapus aktor lain dan filter di-Apply ulang, filter Uploaded By hanya memuat `Wulandari Pengunggah`.
- **Kenyataannya:** FilterContainer/MultiSelect mempertahankan nilai terpilih saat Apply, dan request list tetap mengirim `{"uploadedBy":["Wulandari Pengunggah","Bimo Sementara"]}` (run FileManagerE2-eval-20261112-1520, slot 3). Komponen tidak membuang nilai terpilih secara otomatis; ini sama dengan mayoritas design system (nilai terpilih dikendalikan pemanggil). Konvensi EB-FLT-7 (foundation testcase-conventions L379) menerima salah satu: tetap jalan sebagai snapshot nilai lama, atau ter-reset. PRD File Manager tidak memilih.
- **Karena:** perilaku komponen yang menang (aturan owner 2026-11-04/08), dan pilihan snapshot memenuhi EB-FLT-7.
- **Keputusan:** langkah 33 mengasersi snapshot: kedua nilai tetap terpilih dan dikirim, dan hasil list tetap benar (baris `Bimo Sementara` tidak ada). App tidak menambah prune manual di onApply.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12.
- **Diterapkan di:** skrip FileManagerE2 005 (eval branch `eval/file-manager-e2`).
- **Sumber:** laporan Eval File Manager 2026-11-12; foundation testcase-conventions L379 (EB-FLT-7).

## D-142 Perbedaan tampilan Client Subscription mengikuti UI yang dibangun (2026-11-12)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-013` TC-AC-CS-51 langkah 5 (severity Renew), `TC-AC-CS-E2E-057` TC-AC-CS-212 langkah 9 (perataan [Clear Field] dan [Save]), `TC-AC-CS-E2E-155` TC-AC-CS-590 langkah 5 (ikon Subscription Log `FileHistoryLine`), `TC-AC-CS-E2E-070` TC-AC-CS-270 langkah 5 (tiga kalimat Cancel Request dalam satu paragraf); juga `TC-AC-CS-E2E-145` TC-AC-CS-541 langkah 4 (di luar filter).
- **Spec meminta:** severity tombol, perataan footer, glyph ikon, dan tata letak kalimat yang berbeda dari UI yang dibangun.
- **Kenyataannya:** keempatnya presentasi; perilaku dan setiap kalimat tetap diasersi di langkah yang sama.
- **Karena:** UI yang dibangun adalah acuan untuk presentasi (D-096).
- **Keputusan:** asersi presentasi tersebut keluar dari e2e; perilaku dan teks tetap diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration B).
- **Diterapkan di:** skrip CS 013, 057, 070, 155 (`pending D-draft-CS-UI-PRESENTATION`).
- **Sumber:** repo aplikasi `plans/admin-console-license-allocation-subscription/decisions.md` L389-396 (branch feat/connect-api-b-win e611fc56c).

## D-143 Hari acuan `19/08/26` di spec Client Subscription dijalankan sebagai hari ini (2026-11-12)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-042` TC-AC-CS-162 langkah 11, `TC-AC-CS-E2E-051` TC-AC-CS-199 dan TC-AC-CS-205 langkah 7-8, `TC-AC-CS-E2E-128` TC-AC-CS-473 langkah 19-29; juga `TC-AC-CS-E2E-007` TC-AC-CS-24 (di luar filter).
- **Spec meminta:** jam server dan browser diset ke `19/08/26`, dan tanggal dibaca terhadapnya.
- **Kenyataannya:** tidak ada route yang menggeser jam enterprise-management; helper dev menulis term dengan tanggal literal dan menjalankan satu tick job (`setTenantSubscription`, `runSubscriptionJob`).
- **Karena:** tanggal acuan spec hanya contoh; maksud langkahnya relatif terhadap hari berjalan.
- **Keputusan:** langkah berjalan dengan hari ini (Start Date hari ini, End Date hari ini + 29 hari untuk trial 30 hari). Batas setengah jam setelah tengah malam Asia/Jakarta di TC-AC-CS-473 tidak bisa dibuat dengan tanggal relatif: keluar dari e2e, dan perbandingan zona waktunya dijaga test backend.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration B).
- **Diterapkan di:** skrip CS 042, 051, 128 (`pending D-draft-CS-REFERENCE-DAY`).
- **Sumber:** repo aplikasi `plans/admin-console-license-allocation-subscription/decisions.md` L398-405 (feat/connect-api-b-win e611fc56c).

## D-144 Empty state Default > Active Plans & Features pindah ke ui-client (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-003` TC-AC-PF-19 langkah 1 dan 3.
- **Spec meminta:** sub-tab Default > Active menampilkan empty state asli tanpa CTA.
- **Kenyataannya:** lima plan default (FAMS, SAMS, SIEM) di-seed dan tetap Active; produk tidak punya operasi yang menghapus atau meng-archive semua plan default (`PUT /dev/plans` Dataset E hanya menghapus plan custom dan default yang sudah archived). Hanya intercept yang bisa mengosongkan tab.
- **Karena:** state yang tidak bisa dicapai dengan render murni termasuk ui-client (aturan owner 2026-11-12).
- **Keputusan:** kedua langkah pindah ke spec ui-client (list Default > Active kosong lewat intercept); langkah lain 003 tetap di e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A).
- **Diterapkan di:** skrip PF 003 (`pending D-draft-ACPF-4`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L291.

## D-145 Tombol [Push Update] memakai severity `success` (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-109` TC-AC-PF-275 langkah 9.
- **Spec meminta:** tombol [Push Update] di dialog Push Plan Update berwarna primary.
- **Kenyataannya:** app memakai severity `success`, sesuai konvensi tombol Submit/Save (prd-conventions §24.1 L2589) dan sama dengan tombol submit lain.
- **Karena:** warna tombol adalah presentasi; UI yang dibangun adalah acuan (D-096).
- **Keputusan:** langkah mengasersi `success`.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A).
- **Diterapkan di:** skrip PF 109 (`pending D-draft-ACPF-5`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L300.

## D-146 Link Client Name tetap berwarna sama saat hover (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-160` TC-AC-PF-453 langkah 26.
- **Spec meminta:** link Client Name di tab Assigned Clients berubah warna saat hover.
- **Kenyataannya:** link tetap `#A20F15` saat hover tanpa underline: gaya link DataTable yang sama untuk setiap tabel.
- **Karena:** gaya hover adalah presentasi dan satu keputusan komponen untuk semua screen.
- **Keputusan:** langkah mengikuti UI (warna tetap); bagian tanpa underline tetap diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A).
- **Diterapkan di:** skrip PF 160 (`pending D-draft-ACPF-6`).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L309.

## D-147 Jumlah Clients plan default diasersi dari nilai live, bukan angka spec (2026-11-12)

- **Spec / langkah:** AdminConsole/PlansLicensingPlansFeatures `TC-AC-PF-E2E-001` TC-AC-PF-1 langkah 9; 131 TC-AC-PF-306 langkah 9-10; 133 TC-AC-PF-315 langkah 1-3; 134 TC-AC-PF-321 langkah 11-14; 135 TC-AC-PF-327 langkah 22-25; 136 TC-AC-PF-331 langkah 11; TC-AC-PF-312 langkah 22-27.
- **Spec meminta:** plan seed memegang tepat 12 / 47 / 23 / 8 / 5 Clients.
- **Kenyataannya:** jumlah Clients adalah term Active dan Grace pada plan di seluruh tenant stack (plan-list.md). Plan default dipakai bersama oleh semua tenant yang dibuat dan dihapus suite paralel, jadi jumlahnya berubah selama run; tidak ada seed yang bisa mengunci angka itu tanpa menghapus tenant sesi lain.
- **Karena:** langkah-langkah itu menguji search, filter dan sort kolom Clients, bukan angkanya.
- **Keputusan:** tiap langkah mengasersi terhadap jumlah yang ada di list saat itu (script membacanya lalu menguji search, filter dan sort); angka tepat keluar dari e2e. Gap hanya dibuka bila nilai live tidak bisa membedakan plan.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A).
- **Diterapkan di:** tujuh skrip di atas (`pending D-draft-ACPF-7`, kondisional).
- **Sumber:** repo aplikasi `plans/admin-console-plans-licensing/decisions.md` L318.

## D-148 Nilai kosong Changelog yang disimpan `-` tampil `—` (2026-11-12)

- **Spec / langkah:** GlobalSettings/HardwareHandheldReader `TC-GS-HHR-E2E-063` TC-GS-HHR-345 (Old Value kosong baris Edit), TC-GS-HHR-350 langkah 144, 148, 151 (New Value kosong baris Cancel Request), TC-GS-HHR-351 langkah 166, 170, 173 (New Value kosong baris Delete); `TC-GS-HHR-E2E-061` TC-GS-HHR-336 langkah 98-99. Drift yang sama: AllTags `TC-GS-TAG-E2E-087` TC-GS-TAG-263 langkah 14, `TC-GS-TAG-E2E-089` TC-GS-TAG-268 langkah 29.
- **Spec meminta:** Old Value / New Value kosong tampil `—`; sort menaruh nilai kosong di akhir pada ascending, dan baris non-kosong pertama adalah yang disebut spec.
- **Kenyataannya:** LLD Handheld Reader (L474-L487, L793-L806) dan service menyimpan nilai kosong sebagai `-` (hardware-tagging `LogEmpty = "-"`, hardware-tagging-service#54 ditutup ke kontrak); analytics sudah menghitung `""`, null dan `"-"` sebagai kosong saat filter dan sort. Run hhr-s2-r1: `newValue "-"`. Sel Changelog aplikasi sudah menampilkan `—` untuk `-`, `""` dan null (dicek Integration C 2026-11-12).
- **Karena:** D-054 sudah menetapkan tampilan `—` untuk nilai kosong di semua modul. `-` adalah penanda kosong milik kontrak, bukan data, jadi tampilannya ikut D-054 dan kontrak tidak berubah (opsi b dari usulan). Urutan sort atas nilai non-kosong tidak diatur kontrak.
- **Keputusan:** sel Changelog menampilkan `—` untuk `-`, `""` dan null; langkah tampilan memverifikasi `—` di sel, bukan nilai mentah API. Langkah sort tetap di-skip `feature-gap:be BT-GAP-08 (analytics#56)`; tidak ada asersi `-`.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C, D-draft-HHR-DASH).
- **Diterapkan di:** HHR 061, 063; AllTags 087, 089; AdminConsole Client 120 (TC-AC-ACC-663 langkah 32-33), 134 (TC-AC-ACC-455 langkah 69): Changelog Client (EMS, LLD Client L1145) juga menyimpan `-`. Modal Changelog Client belum dibangun (fase logs, ADR-006), jadi stand-in API mengasersi `-` mentah, dan tampilan `—` menunggu modal di `feature-gap:fe UG-ACC-LOG-1`.
- **Sumber:** repo aplikasi `plans/global-settings-hardware/decisions.md` (blok D-draft-HHR-DASH).

## D-149 Emoji yang disuntik ke DOM Alias Name di luar e2e (2026-11-12)

- **Spec / langkah:** GlobalSettings/HardwareHandheldReader `TC-GS-HHR-E2E-029` TC-GS-HHR-113 langkah 40-45.
- **Spec meminta:** `😊` disuntik langsung ke DOM field Alias Name melewati filter ketikan FE, Save, lalu muncul 422 inline `Alias name contains invalid characters` dengan nilai tetap.
- **Kenyataannya:** pengguna tidak bisa mencapai keadaan itu lewat UI (ketik dan paste ditolak, TC-GS-HHR-112); 422 server untuk `😊` sudah diasersi lewat API di `TC-GS-HHR-E2E-013`.
- **Karena:** e2e hanya membangun keadaan yang benar-benar bisa terjadi; ini cacat spec, bukan wrapper-gap atau library-gap.
- **Keputusan:** blok itu di luar e2e, tanpa langkah dan tanpa gap; tag `@library-gap` dan `@wrapper-gap` dihapus.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-09 (dicatat 2026-11-12, D-draft-HHR-INJECT).
- **Diterapkan di:** `TC-GS-HHR-E2E-029`.
- **Sumber:** repo aplikasi `plans/global-settings-hardware/decisions.md` (blok D-draft-HHR-INJECT).

## D-150 Pesan validasi Custom Field memakai nama field seperti dikonfigurasi (2026-11-12)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-031` TC-GS-USER-155 langkah 30; `TC-GS-USER-E2E-040` TC-GS-USER-215; `TC-GS-USER-E2E-022` TC-GS-USER-158 langkah 60; `TC-GS-USER-E2E-174` TC-GS-USER-1105 langkah 6; NonLoginUser `TC-GS-NLU-E2E-053` TC-GS-NLU-458 langkah 6-7.
- **Spec meminta:** nama field ditulis huruf kecil di pesan V-12 / V-24 (NLU 053: `Badge required`).
- **Kenyataannya:** aplikasi menulis nama Custom Field seperti dikonfigurasi admin (`This Blood Type no longer exists. Please select another.`, `Badge Required must not be empty`); tabel copy PRD memakai placeholder `[Field name]`, bukan nama huruf kecil.
- **Karena:** nama field adalah nama yang diberikan admin; mengecilkannya mengubah nama diri. Ini copy (presentasi), jadi UI yang dibangun menjadi rujukan (D-096).
- **Keputusan:** kelima langkah memverifikasi pesan dengan nama field seperti dikonfigurasi.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** User 022, 031, 040, 174; NLU 053 (D-draft-C-9).
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` L1240.

## D-151 Edit nonaktif pada baris Default User memakai alasan Default User (2026-11-12)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-011` TC-GS-USER-56 langkah 21-23 (TC-GS-USER-57 langkah 36-38 sebagai akibatnya).
- **Spec meminta:** tooltip izin/tier pada item `Edit` yang nonaktif untuk pemegang Full CRUD di baris Default User.
- **Kenyataannya:** aplikasi memberi Edit alasan Default User, sama dengan Delete di bawahnya.
- **Karena:** kondisi baris itu adalah Default User; teks tooltip adalah presentasi, jadi UI yang dibangun menjadi rujukan (D-096).
- **Keputusan:** langkah 21-23 memverifikasi tooltip Default User pada Edit dan Delete.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** User 011 (D-draft-C-11).
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` L1249.

## D-152 Opsi filter Status di popup Select User adalah enum tetap Active / Inactive (2026-11-12)

- **Spec / langkah:** GlobalSettings/NonLoginUser `TC-GS-NLU-E2E-037` TC-GS-NLU-116 langkah 24-25.
- **Spec meminta:** dropdown Status hanya berisi nilai yang ada di tabel (hanya `Active`).
- **Kenyataannya:** `POST /v2/iam/users/options` menjawab `statusOptions` Active dan Inactive; LLD user-crud.md L111 menetapkan opsi Status sebagai enum tetap, bukan facet. Aplikasi memakai opsi dari server apa adanya.
- **Karena:** kontrak menetapkan enum; facet data hanya untuk Position, Division dan referensi lain.
- **Keputusan:** langkah 25 memverifikasi opsi `Active` dan `Inactive`; langkah 26-27 tetap.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-08 (dicatat 2026-11-12, D-draft-S).
- **Diterapkan di:** NLU 037.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` L1258.

## D-153 Badge Dropdown yang dikosongkan kembali ke teks lama tanpa error (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-037` TC-GS-UCF-366 langkah 27-29 dan 30-32.
- **Spec meminta:** error inline `Option name must not be empty` saat badge dikosongkan (atau hanya spasi), lalu `Beta` kembali.
- **Kenyataannya:** BadgeInput dengan `restoreValueOnEmpty` mengembalikan teks lama tanpa error; edit hanya-spasi di-trim menjadi kosong. Run CustomFieldUser-2.
- **Karena:** perilaku komponen menang atas spec (D-096); owner CD-080 (2026-11-08).
- **Keputusan:** langkah 28 dan 31 memverifikasi tidak ada error; langkah 29, 31 dan 32 memverifikasi `Beta` kembali.
- **Diputuskan oleh:** owner CD-080 (2026-11-08), dicatat Wangs-UI Coordinator 2026-11-12 (D-draft-H).
- **Diterapkan di:** UCF 037.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` L1168.

## D-154 Nilai Numeric disimpan dan ditampilkan sebagai angka (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-025` TC-GS-UCF-386 dan TC-GS-UCF-387.
- **Spec meminta:** `-0.0` tersimpan `0.0` dan `5.50` tersimpan `5.50` (seperti diketik).
- **Kenyataannya:** NumberInput selalu menghasilkan angka; nilai tersimpan dan tampil `0` dan `5.5`. Run Rerun-rc44-uifix-3.
- **Karena:** keputusan owner CD-077: Numeric adalah angka, 5.50 == 5.5.
- **Keputusan:** langkah memverifikasi `0` dan `5.5`.
- **Diputuskan oleh:** owner CD-077, dicatat Wangs-UI Coordinator 2026-11-12 (D-draft-J).
- **Diterapkan di:** UCF 025.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-J).

## D-155 Batas 15 digit Numeric menghitung digit nilai angkanya (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-024` TC-GS-UCF-389 langkah 36-43 dan TC-GS-UCF-178 langkah 67-73.
- **Spec meminta:** batas dihitung dari teks yang diketik (`0000000000000001`, 16 karakter, ditolak `Max. 15 characters`).
- **Kenyataannya:** Numeric adalah nilai angka (D-154): `0000000000000001` bernilai `1`; lebih dari 15 digit kehilangan presisi sebagai angka JS.
- **Karena:** keputusan owner CD-077.
- **Keputusan:** nol di depan, `-` dan `.` tidak dihitung; `0000000000000001` diterima; nilai lebih dari 15 digit ditolak `Max. 15 characters`; `-1234567890123.45` diterima dan tersimpan.
- **Diputuskan oleh:** owner CD-077, dicatat Wangs-UI Coordinator 2026-11-12 (D-draft-K).
- **Diterapkan di:** UCF 024.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-K).

## D-156 Numeric tidak menampilkan error untuk `-` atau `.` saja (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-024` TC-GS-UCF-179 langkah 34-35 dan TC-GS-UCF-350 langkah 62-63.
- **Spec meminta:** `-` saja menampilkan `Bonus must be a number`; `.` saja menampilkan `Dec form must be a number`.
- **Kenyataannya:** NumberInput tidak menerima `-` atau `.` saja sebagai nilai dan tidak memunculkan error. Run Rerun-rc46-uifix-4.
- **Karena:** NumberInput menolak ketikan yang membuat nilai tidak valid (perilaku komponen), di atas CD-077.
- **Keputusan:** langkah memverifikasi tidak ada error.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-L).
- **Diterapkan di:** UCF 024.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-L).

## D-157 Menutup Edit User setelah nilai diketik lalu dihapus: tanpa dialog Unsaved Changes (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-021` TC-GS-UCF-188 langkah 46-48.
- **Spec meminta:** setelah Retro Req diisi `x` lalu dikosongkan dan Save ditolak, `[✕]` membuka `Unsaved Changes`.
- **Kenyataannya:** form kembali ke nilai awal (kosong), jadi DialogForm tidak menganggapnya berubah dan `[✕]` menutup popup tanpa dialog. Run Rerun-rc46-uifix-4.
- **Karena:** form dianggap berubah hanya bila nilainya berbeda dari nilai awal, sama seperti di layar lain.
- **Keputusan:** langkah 46-47 memverifikasi popup tertutup tanpa dialog Unsaved Changes.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-M).
- **Diterapkan di:** UCF 021.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-M).

## D-158 Klik backdrop menutup popup All Values (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-002` TC-GS-UCF-15 langkah 27-28.
- **Spec meminta:** klik backdrop tidak menutup popup All Values Preview.
- **Kenyataannya:** popup adalah Dialog Wangs UI (BadgeGroup `+N more`), yang tertutup oleh Escape dan klik backdrop. Run CFU-rerun-rc52.
- **Karena:** perilaku komponen (D-096). Untuk modal Changelog berlaku D-067 (klik backdrop diabaikan).
- **Keputusan:** langkah 28 memverifikasi popup tertutup setelah klik backdrop; popup dibuka lagi untuk langkah 29-30.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-P).
- **Diterapkan di:** UCF 002.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-P).

## D-159 Nilai Dropdown yang basi dilaporkan dengan label yang dikirim (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-038` TC-GS-UCF-368 langkah 70.
- **Spec meminta:** `Beta no longer exists. Please select another.` (label yang dihapus Admin B).
- **Kenyataannya:** sesi A sudah mengganti `Beta` menjadi `Delta` lalu menyimpan; server menolak dengan `Delta no longer exists. Please select another.` Run CFU-rerun-rc52.
- **Karena:** LLD custom-field-user L656: nilai basi dilaporkan dengan label yang dikirim.
- **Keputusan:** langkah 70 memverifikasi `Delta no longer exists. Please select another.`; langkah 72 mengikuti spec.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-Q).
- **Diterapkan di:** UCF 038.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-Q).

## D-160 Error nilai Dropdown muncul saat draft di-commit, bukan saat mengetik (2026-11-12)

- **Spec / langkah:** GlobalSettings/CustomFieldUser `TC-GS-UCF-E2E-017` TC-GS-UCF-66 langkah 47-50, TC-GS-UCF-67 langkah 55-58, TC-GS-UCF-448 langkah 63-66.
- **Spec meminta:** error `Option name already exists` dan `Max. 120 characters` muncul saat mengetik, sebelum Enter.
- **Kenyataannya:** BadgeInput memvalidasi saat draft di-commit (Enter, blur, paste). Run CFU-rerun-rc52.
- **Karena:** perilaku komponen; Ark/Zag dan Mantine TagsInput memvalidasi saat ditambah, antd, MUI dan React Aria tidak memvalidasi saat mengetik.
- **Keputusan:** langkah mengetik draft, menekan Enter, lalu memverifikasi error dan jumlah badge tetap 1.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-R).
- **Diterapkan di:** UCF 017.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-R).

## D-161 Bulk Remove sukses parsial dijalankan admin Manage user and role tanpa Total Control (2026-11-12)

- **Spec / langkah:** GlobalSettings/Role `TC-GS-ROLE-E2E-073` TC-GS-ROLE-261 langkah 34-42.
- **Spec meminta:** aktor Total Control; intercept memalsukan jawaban 200 dengan `failedUserIds`.
- **Kenyataannya:** PRD role.md EC-36: penolakan per baris berlaku untuk aktor non-Total Control; untuk aktor Total Control berlaku EC-34 (diproses lalu auto-revert). Probe slot 3 2026-11-09: `200 "2 deleted, 0 skipped"` dengan `autoRevertedUserIds`.
- **Karena:** dengan aktor Total Control, sukses parsial EC-36 tidak bisa terjadi; jawaban palsu lewat intercept adalah jawaban bisnis. Aktor spec yang keliru, bukan backend.
- **Keputusan:** langkah 34-42 memakai Hendra Wijaya (Manage user and role, tanpa access level); baris kedua diberi Total Control lewat API sebelum `[Remove]`; asersi toast `T-11`, satu baris terhapus, satu tetap, Bulk Action Bar tertutup. Tanpa intercept.
- **Diputuskan oleh:** Wangs-UI Coordinator, 2026-11-09 (dicatat 2026-11-12, D-draft-ROLE-01).
- **Diterapkan di:** Role 073.
- **Sumber:** repo aplikasi `plans/global-settings-role/decisions.md` L270.

## D-162 Bulk Resend yang gagal untuk satu penerima pindah ke ui-client (2026-11-12)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-067` TC-GS-USER-1038 langkah 85-96.
- **Spec meminta:** bulk Resend dengan satu penerima gagal di server, toast `Success, activation email has been sent. Some items failed.`
- **Kenyataannya:** tidak ada route yang menggagalkan satu penerima `POST /v2/iam/users/resend-email`: 5xx menggagalkan seluruh request, chaos Mailpit menggagalkan semua penerima (BT-GS-USER-15, run GSUR-C-3).
- **Karena:** e2e hanya membangun keadaan yang bisa terjadi; hasil parsial adalah tampilan atas jawaban kontrak.
- **Keputusan:** langkah 85-96 pindah ke spec `ui-client` (jawaban parsial lewat intercept dari operasi resend-email di kontrak). BT-GS-USER-15 tetap sebagai kandidat backend saja.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-GSUSER-BULK-RESEND-PARTIAL).
- **Diterapkan di:** User 067.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` L1150.

## D-163 Convert yang bentrok dengan email Login User pindah ke ui-client (2026-11-12)

- **Spec / langkah:** GlobalSettings/NonLoginUser `TC-GS-NLU-E2E-066` TC-GS-NLU-240/444 dan TC-GS-NLU-473 langkah 8-13; `TC-GS-NLU-E2E-068` TC-GS-NLU-244 langkah 4-8 dan TC-GS-NLU-245 langkah 11-14.
- **Spec meminta:** Login User dengan email Non-Login User disisipkan melewati V-09, lalu Convert (tunggal atau bulk) menolak baris itu.
- **Kenyataannya:** Login dan Non-Login User berbagi satu pool email; `POST /v2/iam/users` menjawab 409 `Email already exists` dan email-change menolak email yang sama (BT-GS-NLU-10, run GSUR-C-1). Bentrok tidak bisa terjadi dari browser.
- **Karena:** keadaan yang tidak bisa dicapai produk adalah unit `ui-client`, bukan helper yang merusak cek keunikan backend.
- **Keputusan:** langkah bentrok pindah ke spec `ui-client` penanganan hasil Convert (baris ditolak lewat intercept dari operasi convert di kontrak); langkah lain 066 dan 068 tetap. BT-GS-NLU-10 ditutup sebagai by design.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C) (D-draft-GSNLU-CONVERT-CLASH).
- **Diterapkan di:** NLU 066, 068.
- **Sumber:** repo aplikasi `plans/global-settings-user/decisions.md` (D-draft-GSNLU-CONVERT-CLASH).

## D-164 Klik backdrop tidak menutup dialog penolakan buka produk (2026-11-12)

- **Spec / langkah:** Auth/SessionManagement `TC-AUTH-SES-E2E-030` TC-AUTH-SES-99 (dialog Concurrent session limit reached); `TC-AUTH-SES-E2E-036` TC-AUTH-SES-117 (dialog Subscription Not Active), langkah klik backdrop.
- **Spec meminta:** klik area gelap di luar dialog menutup dialog.
- **Kenyataannya:** dialog tetap terbuka; Escape dan [OK] menutupnya (run 1122). Dialog ini alert Modal Wangs UI, overlay blocking yang tidak ditutup lewat klik backdrop.
- **Karena:** perilaku komponen, sama dengan D-043 (`Modal.spec.md`: "cannot be dismissed by clicking the overlay").
- **Keputusan:** langkah backdrop memverifikasi dialog tetap terbuka; dialog lalu ditutup lewat [OK].
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C).
- **Diterapkan di:** SessionManagement 030, 036.
- **Sumber:** repo aplikasi `plans/auth/integration-findings.md` (triage SES 1122).

## D-165 403 `app_access_denied` saat membuka produk menampilkan popup Access Denied (2026-11-12)

- **Spec / langkah:** Auth/SessionManagement `TC-AUTH-SES-E2E-024` TC-AUTH-SES-74 langkah 26.
- **Spec meminta:** tidak ada dialog setelah 403 `app_access_denied`; FE langsung kembali ke Portal (PRD session-management L299, AUTHSES-LOGIC-04a).
- **Kenyataannya:** aplikasi menampilkan popup "Access Denied" lalu kembali ke Portal setelah [OK].
- **Karena:** override product owner 2026-10-20: setiap 403 `app_access_denied` saat buka produk menampilkan popup Access Denied, sejajar dengan popup D09 (`concurrent_limit_reached`) dan D10 (`subscription_not_active`).
- **Keputusan:** langkah 26 memverifikasi popup Access Denied, [OK], lalu popup tertutup.
- **Diputuskan oleh:** owner (product owner override 2026-10-20), dicatat Wangs-UI Coordinator 2026-11-12.
- **Diterapkan di:** SessionManagement 024.
- **Sumber:** repo aplikasi `plans/auth/decisions.md` L510-514.

## D-166 Delete langsung Client dengan subscription live dijawab 409, bukan 422 (2026-11-12)

- **Spec / langkah:** AdminConsole/Client `TC-AC-ACC-E2E-134` TC-AC-ACC-465 langkah 2, TC-AC-ACC-455 langkah 72-73, TC-AC-ACC-653, TC-AC-ACC-655 langkah 22 dan 24, TC-AC-ACC-978 langkah 31.
- **Spec meminta:** server menolak `DELETE /clients/{id}` langsung dengan `422`.
- **Kenyataannya:** LLD Client menjawab penolakan D-03/D-14 dengan `409` dan `data.errorCode` `delete_blocked_live_subscription` / `delete_blocked_request_in_progress` (admin-console/client LLD L1141, L1253). ems#163 ditutup sesuai LLD; run ACprove-mac-20261112-2014-v1 menjawab 409.
- **Karena:** LLD adalah kontrak; `422` di spec adalah status validasi body (LLD langkah 2), bukan penjaga keadaan.
- **Keputusan:** skrip mengasersi `409` dengan alasan D-03 dan record yang tidak berubah; `422` spec keluar dari e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A, D-draft-ACC-2).
- **Diterapkan di:** Client 134.
- **Sumber:** repo aplikasi `plans/admin-console-client/decisions.md` L62.

## D-167 Notification Center mempertahankan Tab, Search dan Sort saat masuk lagi lewat `[Show All]` (2026-11-12)

- **Spec / langkah:** FixedAsset/Notification `TC-FA-NOTIF-E2E-045` TC-FA-NOTIF-185 langkah 10, `TC-FA-NOTIF-E2E-114` TC-FA-NOTIF-226 langkah 5-8.
- **Spec meminta:** setelah keluar lalu masuk lagi lewat `[Show All]`, Tab, Search dan Sort Notification Center kembali ke default.
- **Kenyataannya:** owner rule state tabel menetapkan bahwa tabel **halaman** (layar list, tab, halaman detail) mempertahankan Search, Filter, Sort, Pagination dan susunan kolom saat pindah tab dan saat dikunjungi lagi; hanya tabel di dalam dialog yang reset (repo aplikasi `plans/_program/prd-overrides.md` L75, product owner 2026-11-11). Notification Center adalah halaman.
- **Keputusan:** skrip mengasersi state yang dipertahankan (Tab, Search, Sort seperti ditinggalkan user); harapan reset di spec keluar dari e2e.
- **Diputuskan oleh:** product owner 2026-11-11 (prd-overrides), dicatat Wangs-UI Coordinator 2026-11-12 (diusulkan Integration N, UG-NOTIF-2).
- **Diterapkan di:** Notification 045, 114.
- **Sumber:** repo aplikasi `plans/notification/integration-findings.md` L49 (row 18).

## D-168 Position yang dipegang user tidak bisa dihapus, jadi state Position basi di Edit Default User tidak tercapai (2026-11-12)

- **Spec / langkah:** AdminConsole/Client `TC-AC-ACC-E2E-069` TC-AC-ACC-474 langkah 20-25 (aktor kedua menghapus Position `Finance Manager` yang dipegang form Edit, lalu Save bertemu "This position no longer exists").
- **Spec meminta:** Position yang sedang dipegang form Edit Default User dihapus saat form terbuka.
- **Kenyataannya:** LLD Position melarang delete Position yang masih dipegang user, login maupun non-login (org-uiux `global-settings/position/API/low-level-design.md` L229-230). Probe slot 2 (2026-11-12): delete Position milik Default User menjawab `0 deleted, 1 skipped`, `blocked` / `in_use`. Position yang tidak dipegang siapa pun tidak muncul sebagai nilai user di dropdown form.
- **Karena:** state itu tidak bisa terjadi di produk; e2e hanya membangun state nyata, dan tidak ada test route yang boleh melanggar LLD.
- **Keputusan:** langkah 20-25 keluar dari e2e. Cek Position basi boleh dipindah ke spec `ui-client` yang meng-intercept jawaban Save. Padanan Division (TC-AC-ACC-152 langkah 11-17) tetap di e2e, karena Division yang dipegang form tapi tidak dipegang user bisa dihapus.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A, D-draft-ACC-1).
- **Diterapkan di:** Client 069.
- **Sumber:** repo aplikasi `plans/admin-console-client/decisions.md` L63-69 (UG-ACC-13, UG-ACC-14).

## D-169 System Limits di bawah rentang hard limit LLD bukan state nyata (2026-11-12)

- **Spec / langkah** (semuanya menyetel limit lewat override System Limits platform, bukan kuota plan, subscription, seat atau device):
  - `masterDataCountLimit` (rentang 1.000–100.000): GlobalSettings Brand 032 TC-233 (13), Brand 033 TC-234 (13), User Custom Field 027 TC-87, 028 TC-454, 029 TC-89 langkah 11-22, Division 020 TC-75 (jumlah+2), 021 TC-74 (jumlah+1), Measurement 022 TC-66 (22), 062 TC-247 (21), Non-Login User 027 TC-100, 121 TC-441 langkah 34-44, Position 015 TC-69, 051 TC-270 langkah 14-30, User 030 TC-149; AdminConsole Device Name 167 TC-AC-DN-605 langkah 26-37 (jumlah katalog sendiri, puluhan). "Kuota gabungan" di NLU 027/121 dan User 030 adalah Master Data Count Limit atas user Login + Non-Login.
  - `selectionLimit` (rentang 100–5.000): AllTags 048 TC-157 (5), Brand 031 TC-127 (10), User Custom Field 043 TC-145 (10), Division 036 TC-129 (5), File Manager 018 TC-75 (5), Handheld Reader 047 TC-221 (5), Measurement 032 TC-112 (10), Position 024 TC-135 (3), User 053 TC-282/283 (3 dan 4).
- **Spec meminta:** menyetel limit ke nilai kecil supaya batas cepat tercapai, lalu mengasersi penolakan atau toast batas.
- **Kenyataannya:** System Limits menolak nilai di luar rentang hard limit dengan `422` "Value must be between …" (org-uiux `admin-console/plans-licensing-lifecycle-settings/API/low-level-design.md` L1165, PRD §9.9). Nilai itu hanya bisa dipasang lewat dev override, jadi tidak pernah terjadi di produk.
- **Karena:** e2e hanya membangun state nyata. State yang tidak mungkin terjadi termasuk cacat spec, bukan helper gap.
- **Keputusan:** langkah-langkah itu keluar dari e2e. Pass lama yang memakai nilai di bawah rentang tidak berlaku (Brand 031/032/033, Measurement 032/062, Division 036, Position 024/015/051, User 030, NLU 027). Spec owner bisa menulis ulang langkahnya pada batas bawah: Selection Limit 100 dengan 101 baris seed, seperti Role 045. Master Data Count dengan 1.000 baris terlalu berat per run, jadi lebih cocok dipindah ke spec `ui-client` yang meng-intercept jawaban batas. Langkah lain di spec yang sama (UCF 029, NLU 121, Position 051) tetap di e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration C; sama dengan Client 306 / UG-ACC-23).
- **Diterapkan di:** 23 spec di atas (22 GS + Device Name 167).
- **Sumber:** repo aplikasi `plans/_program/limit-below-min-2026-11-12.md` (b44c80850).

## D-170 Selection Limit di Client List dibuktikan lewat LCS 166, bukan dengan 130 Client (2026-11-12)

- **Spec / langkah:** AdminConsole/Client `TC-AC-ACC-E2E-306` TC-AC-ACC-448 langkah 2-14 (Selection Limit 100 lalu 120, di atas 130 Client Active tambahan C-SEL-1..130).
- **Spec meminta:** baris setelah batas terkunci, tooltip batas tampil, dan batas baru terbaca tanpa reload, di Client List.
- **Kenyataannya:** nilai 100 dan 120 ada di dalam rentang (org-uiux `admin-console/plans-licensing-lifecycle-settings/API/low-level-design.md` L1165), jadi state-nya nyata. Masalahnya, setiap Client adalah tenant, sehingga 130 Client lewat route asli berarti 130 tenant per run di stack bersama. Client List memakai `SelectionLimitProvider` yang sama dengan Lifecycle Settings. Perilaku batas langsung (baris terkunci, tooltip, batas terbaca ulang tanpa reload) sudah lulus di `TC-AC-LCS-E2E-166` TC-582/583/584 pada 100 dan 120 atas 150 Group (run 1177, 2026-11-12).
- **Karena:** menyiapkan 130 tenant per run tidak sebanding dengan nilainya, karena mekanisme yang sama sudah dibuktikan di LCS 166. Nilai di bawah batas (10/12) yang dulu dipakai stand-in kita bukan dari spec, dan sudah dihapus.
- **Keputusan:** langkah 2-14 keluar dari e2e Client; buktinya dirujuk ke LCS 166. Kalau Client List berhenti memakai provider bersama, keputusan ini dibuka lagi.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration A).
- **Diterapkan di:** Client 306.
- **Sumber:** repo aplikasi `plans/admin-console-client/decisions.md` (UG-ACC-23).

## D-171 Urutan bawaan Customer Subscription: Client A-Z saja, tanpa urutan di dalam Client yang sama (2026-11-12)

- **Spec / langkah:** AdminConsole/CustomerSubscription `001` TC-1 (asersi baris pertama urutan bawaan), `092` TC-349 langkah 5 (urutan Subscription ID di dalam Client yang sama).
- **Spec meminta:** urutan bawaan Client A-Z, lalu Subscription ID terbaru lebih dulu di dalam Client yang sama.
- **Kenyataannya:** LLD list tanpa `sortBy` menulis: tab Current → `LOWER(ce.company_name)` ASC; tab History → `s.created_at` DESC. Tidak ada tie-breaker untuk Client yang sama (org-uiux `admin-console/license-allocation-subscription/API/low-level-design.md` L82). App membuka list tanpa `sortBy`, dan semua ikon sort netral (D-039). Run 1807: dua baris di Client yang sama keluar lama-lalu-baru.
- **Karena:** D-039 menetapkan urutan bawaan = urutan API, dan LLD adalah kontraknya. Urutan di dalam Client yang sama tidak ditulis di kontrak, jadi asersinya termasuk contract drift dan di-skip. Menambah `sortBy` saat dibuka bertentangan dengan ikon netral D-039.
- **Keputusan:** langkah urutan bawaan mengasersi Client A-Z (tab Current) dan ikon sort netral. Urutan baris di dalam Client yang sama tidak diasersi. Asersi baris pertama memilih Client yang namanya paling awal dan unik di data run. Siklus sort per kolom tetap diasersi seperti spec.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration B, FD-B-CS-8).
- **Diterapkan di:** CS 001, 092.
- **Sumber:** repo aplikasi `plans/_program/fail-decisions.md` FD-B-CS-8; perluasan D-039.

## D-172 Banner commit Import menyusun teks dari jumlah record (2026-11-12)

- **Spec / langkah:** GlobalSettings/Import 105, 133, 134, 135, 136, 140, 141, 142, 143, 150, 160, 162, 164, 165, 213, 214, yaitu langkah banner hasil commit.
- **Spec meminta:** teks statis PRD §7 `Success, record has been imported. Duplicate records were ignored.`
- **Kenyataannya:** app menyusun banner dari jumlah record, dengan bentuk tunggal dan jamak: `Success, N record(s) have been imported.`, lalu kalimat duplikat dan `N error(s) remain.` hanya kalau berlaku. Contohnya `Success, 12 records have been imported.` (run 1908). Ini keputusan slicing yang dicatat di repo aplikasi `plans/global-settings-import/decisions.md` L255.
- **Karena:** teks statis tidak bisa membawa angka yang justru diasersi spec sendiri (`N errors remain.`). Pesan status dengan jumlah ber-plural adalah pola umum (notifikasi MUI, antd, Mantine). Bedanya hanya soal kata dan bentuk (D-096), bukan aturan bisnis.
- **Keputusan:** langkah banner mengasersi teks lengkap yang disusun dari jumlah yang diketahui langkah itu: jumlah yang diimpor, kalimat duplikat kalau ada duplikat, dan jumlah error yang tersisa. Kalimat statis PRD tidak diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-12 (diusulkan Integration B, FD-B-IMP-13).
- **Diterapkan di:** 16 spec Import di atas.
- **Sumber:** repo aplikasi `plans/_program/fail-decisions.md` FD-B-IMP-13; `packages/features/global-settings-import/resources/Strings.ts` L134-139.

## D-173 Form Device SKU mempertahankan ketikan setelah save ditolak karena stok (2026-11-13)

- **Spec / langkah:** AdminConsole/SettingsDeviceSku `074` TC-AC-DS-237 langkah 20-21.
- **Spec meminta:** setelah Save ditolak karena SKU sudah punya stok (referensi basi), form dimuat ulang ke nilai yang tersimpan.
- **Kenyataannya:** `PATCH /device-skus/{id}` → 422 `SKU code cannot be changed after stock has been registered` (run 1209). App menampilkan toast error, menyegarkan kunci (SKU code, Device Name dan Range Type terkunci, langkah 22 lulus), dan mempertahankan ketikan pengguna. Form tetap dirty, jadi [✕] menampilkan Unsaved Changes. PRD (settings-device-sku ACDS-LOGIC-03b, L159) hanya mengatur penguncian dan tidak mengatur isi form setelah penolakan.
- **Karena:** keputusan owner E2E-DS-105 (2026-11-11) menetapkan nilai pengguna dipertahankan setelah save terkunci ditolak. Mempertahankan input setelah penolakan server juga perilaku form mayoritas design system, dan form Device Name di app yang sama berlaku begitu.
- **Keputusan:** langkah 20-21 mengasersi bahwa nilai ketikan dipertahankan, field terkunci, dan [✕] menampilkan Unsaved Changes. Tag UG-DS-11 dilepas.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (diusulkan Integration C, FD-C-11).
- **Diterapkan di:** DS 074.
- **Sumber:** repo aplikasi `plans/_program/fail-decisions.md` FD-C-11; `integration-findings` E2E-DS-105.

## D-174 Urutan baris dengan nilai sama di File Manager mengikuti tie-break LLD (2026-11-13)

- **Spec / langkah:** GlobalSettings/FileManagerE2 `003` (l.13-14, 30-31, 40, 64-66) dan `017` (Deleted By), serta spec File Manager lain yang mengasersi urutan di antara baris bernilai sama.
- **Spec meminta:** baris bernilai sama diurutkan dari yang terbaru (EB-SRT-2).
- **Kenyataannya:** LLD File Manager menulis "Secondary sort: Always apply secondary tie-break on fmd.id in the same direction" untuk list (L114, BEGAP-210) dan Recycle Bin (L550). Service mengikuti aturan itu, sehingga pada sort ASC baris bernilai sama muncul dengan id menaik, dan pada DESC dengan id menurun.
- **Karena:** LLD adalah kontrak (D-039, D-171), dan tie-break-nya ditulis eksplisit dan deterministik.
- **Keputusan:** urutan di antara baris bernilai sama diasersi menurut tie-break LLD, yaitu `id` searah dengan arah sort, bukan "terbaru dulu". D-draft-FILEMGR2-SORT-1 menjadi entri ini.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (diusulkan Eval FM r2).
- **Diterapkan di:** FileManagerE2 003, 017.
- **Sumber:** org-uiux `global-settings/file-manager/API/low-level-design.md` L114, L550.

## D-175 D-112 ditarik: pengganti trial tidak mencapai Waiting for Approval (2026-11-13)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `TC-AC-CS-E2E-074` (langkah yang diatur D-112), serta langkah Waiting-trial di 057, 058, 060, 062, 070 dan 071.
- **Spec meminta:** request dari entity Distributor/Partner (Fajar, PT Maju Bersama; Rina, CV Karya Mandiri) yang menunggu approval.
- **Kenyataannya:** LLD `POST /subscriptions/trials` step 6 (L1180) menetapkan bahwa trial dari aktor entity Principal langsung `active`. Hanya trial dari Distributor/Partner dengan `require_approval_for_trial = true` yang menjadi `waiting_for_approval`. Pengganti di D-112 (trial oleh requester di entity Principal) karena itu langsung Active (run CS-AdminConsole-win-20261113-e, term 2121039185581182977), jadi blok cancel-while-Waiting tidak tercapai. Aksi dan rute untuk entity Distributor/Partner belum ada di sprint (ems#52/#83).
- **Karena:** pengganti tidak membentuk state yang diuji, dan state yang benar hanya bisa dibuat dari entity yang belum masuk sprint.
- **Keputusan:** D-112 ditarik. Langkah Waiting-trial di spec di atas menjadi `sprint-gap` (ems#52/#83), dan kembali dijalankan dengan persona spec saat entity Distributor/Partner masuk sprint. Cabang renew tetap `sprint-gap` pricing.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (diusulkan Integration B).
- **Diterapkan di:** skrip LicenseAllocationSubscription 057, 058, 060, 062, 070, 071, 074.
- **Sumber:** org-uiux `admin-console/license-allocation-subscription` LLD L1180; be-filing 0185d69 (BT-AC-CS-22 bagian 8).

## D-176 Langkah Modified By di User 071 memakai pengubah buatan run, bukan baris `System` (2026-11-13)

- **Spec / langkah:** GlobalSettings/User `TC-GS-USER-E2E-071` TC-GS-USER-419 langkah 98 dan 108.
- **Spec meminta:** baris dengan `Modified By = System` muncul (Search lalu tampilkan kolom Modified By).
- **Kenyataannya:** satu-satunya baris `System` adalah Default User hasil seed. Spec 032 (TC-GS-USER-162) mengedit Default User itu, sehingga Modified By-nya berganti. Langkah 98/108 lulus hanya kalau 071 berjalan sebelum 032. Urutan itu hanya dijaga `serial-specs.txt` (D-314) di runner penuh. Run 1190 (urutan 032 lalu 071) tidak punya baris `System` sama sekali.
- **Karena:** spec tidak boleh bergantung pada urutan spec lain, dan baris yang diasersi harus milik spec itu sendiri.
- **Keputusan:** langkah 98 dan 108 mengasersi nama pengubah yang dibuat run (seperti D-132: login user `Pengubah <runId>-071` mengedit U-1 lalu dihapus). Yang diasersi: Search nama itu, lalu baris U-1 menampilkan nama itu di Modified By, karena Modified By menyimpan snapshot nama. Ketergantungan urutan D-314 untuk 071 dihapus.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (diusulkan Integration C, FD-C-4).
- **Diterapkan di:** User 071.
- **Sumber:** repo aplikasi `plans/_program/fail-decisions.md` FD-C-4; run 1190.

## D-177 Baris Changelog Renew terjadwal mengikuti LLD: field `Status`, bukan Plan/End Date (2026-11-13)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `076` TC-288 dan `113` TC-438.
- **Spec meminta:** baris Changelog Renew (efek terjadwal) dengan Field `Plan`/`End Date`, misalnya `Growth/dd/MM/yy` → `Professional/dd/MM/yy`.
- **Kenyataannya:** LLD license-allocation-subscription mencatat satu baris Changelog `Renew (efek terjadwal, diterapkan)` dengan field `Status` (Renew endpoint, Logs Written L989 dan contoh L991-L1007; Background Jobs, Scheduled flip, Mode Renewal L2127). Plan dan End Date adalah detail Subscription Log `Subscription renewed`, bukan baris Changelog. Stack menulis sesuai LLD: `Status` `Pending` → `Active`, Modified By System.
- **Karena:** PRD vs LLD adalah contract drift. Aturan owner (2026-11-08): drift diskip, tanpa improvisasi.
- **Keputusan:** asersi Plan/End Date di baris Changelog Renew pada kedua langkah itu diskip sebagai contract drift. Baris `Status` tidak diasersi sebagai pengganti. Detail Plan/End Date di Subscription Log tetap di gate BT-GAP-60 (ars#65) dan BT-AC-CS-35 (ems#206: Flip menulis `Subscription renewed` tanpa detail).
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (temuan Integration B, run l; cek LLD oleh sesi BE).
- **Diterapkan di:** LicenseAllocationSubscription 076, 113.
- **Sumber:** LLD admin-console/license-allocation-subscription L989, L991-L1007, L2127; repo aplikasi `plans/_program/fail-decisions.md`.

## D-178 Nama objek baris Changelog term subscription memakai suffix kode produk (2026-11-13) (ditarik oleh D-179)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `113` TC-456 langkah 44 dan 46, dan `079` TC-296.
- **Spec meminta:** baris Changelog Trial dengan nama objek `<Client>` saja.
- **Kenyataannya:** LLD license-allocation-subscription menetapkan `objectName = entities.company_name || ' — ' || products.code` untuk semua baris Changelog term: Trial create L1234, Add L661 (contoh L654), Edit L888 (contoh L881), Renew L1007 (contoh L1000). Job Timeout Auto-Cancel dan Scheduled Flip (L2108-L2172) mengikuti aturan yang sama. Contoh JSON Trial create L1245 (`"PT Bintang Timur"` tanpa suffix) bertentangan dengan rumus prosa dan tiga contoh lain, jadi itu ketidakkonsistenan dokumen. PRD tidak mendefinisikan nilai nama objek. Stack menulis `<Client> — <kode produk>`, misalnya `… — SIEM`.
- **Karena:** PRD diam soal nilai ini, sehingga LLD yang menjadi kontrak. Ini bukan drift yang diskip.
- **Keputusan:** langkah-langkah itu mengasersi nama objek `<Client> — <kode produk>` sesuai rumus LLD. Ketidakkonsistenan contoh L1245 diteruskan ke pemilik LLD.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (temuan Integration B run 1251; cek LLD oleh sesi BE).
- **Diterapkan di:** LicenseAllocationSubscription 079, 113.
- **Sumber:** LLD admin-console/license-allocation-subscription L654, L661, L881, L888, L1000, L1007, L1234, L1245, L2108-L2172.

## D-179 D-178 ditarik: nama objek baris Changelog Trial adalah drift PRD vs LLD, diskip (2026-11-13)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `113` TC-456 langkah 44 dan 46, dan `079` TC-296 (asersi nama objek baris Changelog Trial).
- **Dasar D-178 keliru:** D-178 menyatakan PRD tidak mendefinisikan nama objek. Ternyata PRD license-allocation-subscription §4.1.2 L625 dan §8.1 menetapkan sel "Client — Product" untuk baris Trial berisi `[Client Name]` saja (Activate L1474, Edit Trial L1487-L1490, Cancel Request (Trial) L1495, Timeout Auto-Cancel (Trial) L1496, Resubmit (Trial) L1497). Baris paid berisi `[Client Name] — [Product Name]`. Contoh JSON LLD L1245 sesuai PRD, sedangkan rumus prosa LLD L1234 (dan stack) menulis `<Client> — <kode produk>`.
- **Karena:** ini contract drift PRD vs LLD. Aturan owner: drift diskip, dan issue diposting supaya LLD diperbaiki (owner 2026-11-13).
- **Keputusan:** asersi nama objek baris Changelog Trial pada langkah-langkah itu diskip dengan gate `BT-AC-CS-37` (enterprise-management-service#224), sampai pemilik LLD/PRD memutuskan. Tidak ada asersi pengganti. D-178 ditarik.
- **Diputuskan oleh:** Wangs-UI Coordinator di bawah delegasi owner (2026-10-31), 2026-11-13 (koreksi dari sesi BE).
- **Diterapkan di:** LicenseAllocationSubscription 079, 113.
- **Sumber:** PRD license-allocation-subscription L625, L1474, L1487-L1490, L1495-L1497; LLD L1234, L1245; enterprise-management-service#224.

## D-180 Waktu caption lock login memakai Time Format default dan timezone pengguna, bukan setelan tenant (2026-11-13)

- **Spec / langkah:** Auth/LoginPassword `TC-AUTH-LP-E2E-040` TC-138 langkah 41-42.
- **Spec meminta:** waktu boleh-coba-lagi di caption lock (15 menit/1 jam) mengikuti Time Format dan zona General Settings tenant (PRD S-AUTHLP-03 L210, D-29).
- **Kenyataannya:** halaman login publik. Login yang gagal tidak punya sesi, jadi tidak bisa membaca setelan tenant, dan memang tidak boleh. Jawaban `outcome: locked` hanya membawa `lockUntil` (instan UTC). LLD/openapi (L543, L662-664) menetapkan FE yang memformat `lockUntil` (jam dan menit saja).
- **Keputusan (owner):** waktu di caption = `lockUntil` diformat dengan opsi Time Format default (`HH:mm`), di timezone pengguna sendiri (browser), bukan setelan tenant. Langkah 41-42 mengasersi format itu, dengan waktu dihitung dari `lockUntil` dalam zona browser run. iam-service#185 (BT-AUTH-LP-1) ditutup sebagai bukan defect. PRD akan diperbarui owner.
- **Diputuskan oleh:** owner (Zain), 2026-11-13. Dicatat oleh Wangs-UI Coordinator.
- **Diterapkan di:** LoginPassword 040.
- **Sumber:** repo aplikasi `plans/_program/prd-overrides.md` (baris auth/login-password, 2026-11-13); iam-service#185; openapi auth/login-password L543, L662-664.

## D-181 Form Add Subscription: Product baru bisa dipilih setelah Client dipilih (2026-11-13)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `030` TC-112 langkah 2.
- **Spec meminta:** memilih Product SAMS di form Add tanpa memilih Client lebih dulu.
- **Kenyataannya:** PRD §4.3 (tabel field form Add, baris Product) membatasi opsi Product pada FAMS/SAMS/SIEM yang belum punya baris di tab `Current` **untuk Client terpilih**, jadi daftar Product bergantung pada Client. Aplikasi baru memuat opsi Product setelah Client dipilih, sesuai PRD.
- **Keputusan:** langkah 2 diawali memilih Client yang memenuhi syarat, lalu memilih Product SAMS. Asersi tentang Product dan Plan tetap seperti di spec. Aplikasi tidak diubah.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-13.
- **Diterapkan di:** LicenseAllocationSubscription 030.
- **Sumber:** PRD license-allocation-subscription §4.3 baris Product (L427); `useSubscriptionFormDialogViewModel.ts` L283-289.

## D-182 Field IMEI Add Stock menyaring input: hanya digit, berhenti di 15 (2026-11-13)

- **Spec / langkah:** AdminConsole/TagStock `TC-AC-ACTS-E2E-085` TC-247, langkah yang mengetik IMEI 16 digit, IMEI berhuruf, dan IMEI berspasi.
- **Spec meminta:** input tidak valid itu diketik apa adanya lalu ditandai tidak valid.
- **Kenyataannya:** field IMEI di Add Stock (helper PRD tag-stock L1032 "Digits only, exactly 15 digits.") menyaring input saat diketik: huruf dan spasi dibuang, dan input berhenti di 15 digit. Jadi ketiga input itu tidak bisa ada di field. Pola yang sama dengan D-016 (emoji dibuang di level input).
- **Keputusan:** perilaku komponen menang. Langkah itu mengasersi isi field setelah diketik: hanya digit, maksimal 15 digit pertama. IMEI yang tetap tidak valid setelah disaring (kurang dari 15 digit, mis. `12345`) tetap diasersi sebagai Invalid Format sesuai PRD L470/L481/L494.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-13.
- **Diterapkan di:** TagStock 085.
- **Sumber:** PRD tag-stock L470, L481, L494, L1032; D-016.

## D-183 Note User Log untuk Login dan Logout mengikuti kanon auth-foundation (2026-11-14)

- **Spec / langkah:** GlobalSettings/User `148` TC-GS-USER-933 langkah 11, TC-GS-USER-935.
- **Spec meminta:** kolom Note di User Log berisi `—` untuk Login sukses dan Logout biasa (mengikuti contoh tabel PRD user.md §8.4 L785/L787).
- **Kenyataannya:** user.md L4 merujuk `auth-foundation.md` §9 sebagai kanon User Log. Kanon itu menulis Note `Login with password` untuk login sukses dengan password (L320, L493) dan `Logged out` untuk logout manual (L386). Backend menulis persis itu, dan Auth LoginPassword 126/039 mengasersi teks yang sama. Contoh di user.md §8.4 hanya ilustrasi.
- **Keputusan:** Note diasersi sesuai kanon auth-foundation §9 (`Login with password`, `Logged out`). Kolom Status tetap `—` untuk Logout dan Session (auth-foundation L485).
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** User 148. Diperluas 2026-11-14: TC-GS-USER-938 (Reset Password sukses) mengasersi Note `Password updated successfully` sesuai auth-foundation L505, L516, L628 dan reset-password L799, bukan `Reset password via email link`; berlaku sama untuk Note User Log lain yang tertulis di kanon auth-foundation §9.
- **Sumber:** auth-foundation.md L320, L386, L485, L493; user.md L4, L785, L787; prd-gap-registry GAP-306.

## D-184 Submit import GPS lebih dari 5.000 baris kembali ke Detail SKU, Preview tidak tetap tampil (2026-11-14)

- **Spec / langkah:** AdminConsole/TagStock `092` TC-AC-ACTS-771 langkah 7-9 dan TC-AC-ACTS-772 langkah 21-23 (juga 887 bila memakai langkah yang sama).
- **Spec meminta:** setelah `[Submit]` pada Preview lebih dari 5.000 baris, Preview tetap tampil, lalu ditutup lewat `[Cancel]` → Unsaved Changes → `[Leave]`.
- **Kenyataannya:** PRD tag-stock L1056 menyatakan Submit di atas 5.000 baris tetap mengikuti tiga cabang `FI-05`, dengan request langsung kembali membawa T-23. `FI-05` (L900) menetapkan: "Setelah `[Submit]` berhasil, user selalu kembali ke Detail SKU > Tab Available SKU tersebut". Aplikasi melakukan itu, sama seperti jalur sinkron.
- **Keputusan:** langkah Cancel/Leave setelah Submit tidak dijalankan karena tidak ada di alur PRD. Sebagai gantinya diasersi toast T-23 (`"Preparing your import. We'll notify you when it's ready."`) dan halaman Detail SKU tab Available. Ini bukan ui-gap. Aplikasi tidak diubah.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** TagStock 092 (dan 887 bila berlaku).
- **Sumber:** PRD tag-stock L900 (FI-05), L1056, L1969 (T-23).

## D-185 Bulk Delete Device Name: ID yang sudah dihapus admin lain dihitung terhapus, bukan "skipped" (2026-11-14)

- **Spec / langkah:** AdminConsole/SettingsDeviceName `184` TC-233 dan `185` TC-579.
- **Spec meminta:** bila salah satu ID terpilih sudah dihapus admin lain, toast menyebut "Some items were skipped".
- **Kenyataannya:** PRD settings-device-name T-08 (L555) memakai "Some items were skipped" hanya untuk item yang diblok ("still has SKUs or registered devices"). LLD DELETE (L406, L409) memperlakukan ID yang sudah tidak ada sebagai idempoten: dilaporkan `status: deleted`, dan pesan 200-nya `Success, device name has been deleted.` bila tidak ada yang diblok.
- **Keputusan:** langkah itu mengasersi toast sukses biasa `"Success, device name has been deleted."` tanpa kalimat skipped. Bila semua ID sudah tidak ada (204), berlaku T-09 `"This device name is no longer available."` (PRD L556).
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** SettingsDeviceName 184, 185.
- **Sumber:** PRD settings-device-name L555, L556; LLD settings-device-name L406, L409, L456.

## D-186 Edit CRUD atas target yang tier-nya berubah sejak render: checkbox mengikuti nilai terbaru dari server (2026-11-14)

- **Spec / langkah:** AdminConsole/SettingsRolePermission `118` TC-AC-RP-400 langkah 37-39.
- **Spec meminta:** setelah PATCH ditolak `403 target_tier` (target baru dijadikan Total Control oleh sesi lain), langkah 38 meminta checkbox "kembali ke nilai semula" (tidak tercentang, nilai saat render), sedangkan langkah 39 meminta baris di-refresh.
- **Kenyataannya:** kedua langkah bertentangan untuk target Total Control, karena baris yang di-refresh menampilkan C/R/U/D tercentang. PRD settings-role-permission L815 dan L1727: aksi tulis atas baris yang sudah berubah tier oleh admin lain sejak render → toast netral `"This permission is no longer available."` dan "data di-refresh ke nilai terbaru, perubahan tidak tersimpan".
- **Keputusan:** langkah 38 mengasersi checkbox pada nilai terbaru dari server setelah refresh (untuk target Total Control: tercentang), bukan nilai saat render. Refresh baris (langkah 39) diasersi seperti di spec. Spec tidak meminta toast, tetapi PRD L815/L1727 meminta toast netral `"This permission is no longer available."`, jadi toast itu ikut diasersi. Aplikasi diperbaiki supaya `403 target_tier` menampilkan toast netral itu, bukan teks mentah `Forbidden`.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** SettingsRolePermission 118; GlobalSettings Role 103 TC-273 langkah 31 (2026-11-14: setelah `403 target_tier`, checkbox target yang kini Total Control tercentang dan disabled sesuai refresh).
- **Sumber:** PRD settings-role-permission L815, L1727.

## D-187 Pesan error Field menggantikan helper text (2026-11-14)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `160` TC-AC-CS-485 langkah 11-13 (Activate Trial, batas Trial Duration).
- **Spec meminta:** setelah mengetik 46, helper `"Maximum 45 days"` tetap tampil bersama pesan error validasi.
- **Kenyataannya:** komponen Field Wangs UI menampilkan pesan error di tempat helper text, sehingga helper tidak tampil selama ada error. Ini perilaku mayoritas design system (MUI `helperText` diganti error, Chakra `FormHelperText` vs `FormErrorMessage`, React Spectrum `description` diganti `errorMessage`). Aplikasi tidak menyembunyikan helper sendiri.
- **Keputusan:** perilaku komponen menang. Helper `"Maximum 45 days"` diasersi sebelum nilai tidak valid diketik. Setelah 46 diketik, yang diasersi pesan error dan nilai batas yang dibaca live, tanpa helper.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** LicenseAllocationSubscription 160; berlaku sama untuk spec lain yang mengharapkan helper dan error tampil bersamaan pada satu Field.
- **Sumber:** perilaku komponen Field Wangs UI; aturan perilaku komponen mengikuti mayoritas design system.

## D-188 Activate Trial: field Trial Asset Quota baru tampil setelah Product FAMS/SAMS dipilih (2026-11-14)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `046` TC-AC-CS-176 langkah 5.
- **Spec meminta:** field Trial Asset Quota (placeholder `"Enter asset quota"`, helper `"Maximum 200 assets"`) tampil di form Activate Trial sebelum Product dipilih.
- **Kenyataannya:** PRD license-allocation-subscription L516 menyatakan Asset Quota "Tampil hanya FAMS/SAMS", dan L513 menyatakan Product "menentukan field quota mana yang tampil". Sebelum Product dipilih, field quota tidak tampil.
- **Keputusan:** langkah 5 mengasersi Trial Asset Quota (placeholder dan helper) setelah Product FAMS atau SAMS dipilih. Spec ini cacat untuk urutan tersebut, bukan UI.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** LicenseAllocationSubscription 046.
- **Sumber:** PRD license-allocation-subscription L513, L516.

## D-189 Pin kolom maksimal 3 per tabel (2026-11-14)

- **Spec / langkah:** AdminConsole/SettingsUser `085` langkah 41 (pin 9 kolom) dan `086` langkah 24 (pin 5 kolom); berlaku sama untuk spec lain yang mem-pin lebih dari 3 kolom.
- **Spec meminta:** lebih dari 3 kolom di-pin sekaligus di Setup Column.
- **Kenyataannya:** prd-conventions §9 L1455 membatasi pin maksimal 3 kolom per tabel (kolom Checkbox dan Actions tidak dihitung). Komponen Setup Column Wangs UI menerapkan batas itu (`maxPinnedColumns` default 3).
- **Keputusan:** spec cacat pada jumlah pin. Skrip mem-pin 3 kolom pertama yang diminta spec, lalu mengasersi pin kolom ke-4 tidak bisa diaktifkan (disabled) dan hint batas tampil. Langkah lanjutan yang membaca kolom ter-pin memakai 3 kolom itu.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** SettingsUser 085, 086.
- **Sumber:** org-uiux foundation prd-conventions §9 L1455.

## D-190 Activate Trial: plan default di-archive di antara isi form dan Submit tidak diuji di e2e (2026-11-14)

- **Spec / langkah:** AdminConsole/LicenseAllocationSubscription `048` TC-AC-CS-186 langkah 17-26.
- **Spec meminta:** form Activate Trial diisi dengan plan default `Growth`, plan itu di-archive lewat API sebelum [Submit], lalu muncul error inline V-17 `"This plan no longer exists. Please select another."`, field Plan dikosongkan, dan opsinya dimuat ulang tanpa Growth.
- **Kenyataannya:** dropdown Plan trial hanya berisi plan default aktif (LLD license-allocation-subscription L411), jadi plan Custom milik run tidak bisa menggantikannya. Plan default FAMS dipakai bersama semua spec di stack, dan archive plan default tidak bisa dibatalkan (tidak ada un-archive di API Plans & Features). Plan default milik run juga tidak bisa dibuat: `POST plans-features/default` menjawab `409 "This product already has the maximum number of paid plans (3)"` (slot 3, 2026-11-14). State itu hanya bisa dibentuk dengan merusak data bersama atau lewat route dev.
- **Keputusan:** langkah 17-26 keluar dari e2e. Validasi ulang server V-17 dijaga unit test backend. Penanganan UI atas jawaban V-17 (error inline, Plan dikosongkan, opsi dimuat ulang) dijaga di lapisan ui-client dengan respons yang di-intercept. Langkah 1-16 tetap berjalan, dan 048 tidak lagi masuk serial-specs.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** LicenseAllocationSubscription 048.
- **Sumber:** PRD license-allocation-subscription L512 (V-17); LLD license-allocation-subscription L410-L411; respons 409 plans-features/default (run CS-048-win-20261114-d).

## D-191 Teks dialog auto-revert Read Only mengikuti copy PRD (2026-11-14)

- **Spec / langkah:** GlobalSettings Role `048` TC-295 langkah 35; berlaku sama untuk spec lain yang menulis teks dialog auto-revert Read Only berbeda dari copy PRD.
- **Spec meminta:** dialog berbunyi `"Editing this permission will remove Read Only access from this user…"`.
- **Kenyataannya:** copy baku dialog auto-revert di prd-conventions L2352 (dan copy D-02 PRD Role) adalah `"This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited. …"`, dan aplikasi menampilkannya persis. Teks spec tidak cocok dengan sumber copy mana pun.
- **Keputusan:** copy PRD menang. Skrip mengasersi teks prd-conventions L2352.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** GlobalSettings Role 048.
- **Sumber:** org-uiux foundation prd-conventions L2352.

## D-192 Save Lifecycle Settings dengan nilai null atau tipe salah dijawab 422 dengan pesan tipe dari LLD (2026-11-14)

- **Spec / langkah:** AdminConsole/PlansLicensingLifecycleSettings `173`-`176`, `178`-`180`: langkah permintaan Save langsung ke server dengan field dikosongkan (null) atau bertipe salah (desimal, string), misalnya TC-AC-LCS-612, 613, 616, 620, 624, 628, 632, 636.
- **Spec meminta:** permintaan ditolak server dengan status `400` ("field wajib terisi").
- **Kenyataannya:** LLD plans-licensing-lifecycle-settings L62 dan L150 (juga L148, L313; openapi L149, L181-184): JSON yang tidak bisa di-parse → `400`; field `null` → `422` `"Expected integer, but received null"` (`"Expected boolean, but received null"` untuk `requireApprovalForTrial`); tipe salah → `422` `"Expected integer, but received <type>"`. Backend menjawab persis seperti itu sejak dev 42bf76d (2026-11-11).
- **Keputusan:** kontrak LLD menang. Langkah tersebut mengasersi `422` dengan pesan tipe dari LLD, bukan `400`. Langkah reload yang memastikan nilai tersimpan tidak berubah tetap diasersi seperti di spec. Menggantikan D-draft-LCS-1.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** PlansLicensingLifecycleSettings 173, 174, 175, 176, 178, 179, 180.
- **Sumber:** LLD plans-licensing-lifecycle-settings L62, L148, L150, L313; run LCS-b-win-20261114-l (board 1387).

## D-193 Request tulis langsung atas Client Archived ditolak 409 `client_not_active` (2026-11-14)

- **Spec / langkah:** AdminConsole/Client `131` TC-AC-ACC-907 langkah 14 (resend activation email) dan TC-AC-ACC-906 langkah 19 (toggle BYO activation setting); berlaku sama untuk request tulis langsung lain atas Client Archived.
- **Spec meminta:** server menolak dengan `403 Forbidden`.
- **Kenyataannya:** LLD client L1425, L1517 dan L1536 (openapi L1608, L1782): `403` hanya untuk gerbang permission (sebelum lookup) dan untuk Client Suspended (`workspace_suspended`); Client Archived dijawab `409` dengan `data.errorCode` `client_not_active`. Backend menjawab persis seperti itu.
- **Keputusan:** kontrak LLD menang. Langkah tersebut mengasersi penolakan `409` dengan `client_not_active`, dan langkah sesudahnya (tidak ada email yang terkirim, setting tidak berubah) tetap diasersi. Menggantikan D-draft-ACC-ARCHIVED-WRITE-STATUS.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** Client 131.
- **Sumber:** LLD admin-console client L1425, L1517, L1536; openapi L1608, L1782.

## D-194 Edit pertama Login User hasil Convert wajib memilih Access (2026-11-14)

- **Spec / langkah:** GlobalSettings/NonLoginUser `116` TC-GS-NLU-428 langkah 24-26.
- **Spec meminta:** user hasil Convert diedit hanya First Name-nya (`Sudah` → `Sudahx`), lalu [Save] dan popup Edit menutup.
- **Kenyataannya:** PRD non-login-user L230: setelah Convert, akun berstatus Pending Activation dengan 0 Access sebagai keadaan transisi, dan validasi minimal 1 Access berlaku pada Edit berikutnya (user.md §9.9, V-15 L1436: `"Access must not be empty"`). Edit yang hanya mengubah First Name tidak bisa disimpan, dan popup tetap terbuka dengan error V-15.
- **Keputusan:** langkah 25 mengubah First Name dan memilih satu Access dalam Edit yang sama sebelum [Save], seperti yang dilakukan admin menurut PRD. Langkah lanjutan yang membaca Changelog menerima entri Access yang ikut tercatat.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** NonLoginUser 116.
- **Sumber:** PRD non-login-user L230; PRD user L1436 (V-15).

## D-195 Pembacaan Hardware Stock di spec HHR: kondisi Client, log Hardware Stock, dan total unit (2026-11-14)

- **Spec / langkah:** GlobalSettings/HardwareHandheldReader `068` (TC-GS-HHR-376..382), `069` (TC-GS-HHR-387, 388), `077` (TC-GS-HHR-375); berlaku sama untuk spec lain yang membaca Hardware Stock dengan istilah yang sama.
- **Spec meminta:** membaca `Client Reported Condition` dan `Status` unit, "Changelog Hardware Stock", dan "total unit Hardware Stock".
- **Kenyataannya:** Stock Detail tidak punya kolom `Client Reported Condition`; kondisi laporan Client tampil di sel `Status` Tab In Use (PRD hardware-stock §4.1.5). Hardware Stock tidak punya tombol Changelog; riwayat operasinya ada di Activity Log §8.2 (`change_logs`, PRD L1713, L1742), termasuk `Device Released` dan `Device Activation Canceled`. Stock List Principal memuat SKU suite lain, jadi total seluruh list tidak deterministik.
- **Keputusan:** (1) `Client Reported Condition` = sel `Status` Tab In Use, dan "Status tidak berubah" = tab yang memuat unit itu (In Use/Available). (2) "Changelog Hardware Stock" = baris Activity Log Object `Hardware` (§8.2). (3) "Total unit Hardware Stock" = jumlah `Total Registered` baris Stock List dari SKU katalog Handheld Reader milik spec (Search `SKU-HHR`).
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (wewenang malam 2026-11-13), 2026-11-14.
- **Diterapkan di:** HardwareHandheldReader 068, 069, 077.
- **Sumber:** PRD admin-console hardware-stock §4.1.5, L1713, L1742.

## D-196 Klik backdrop pada popup Change Password mengikuti perilaku DialogForm (2026-11-14)

- **Spec / langkah:** GlobalSettings/MyProfile `025` TC-GS-PROFILE-150 langkah 17-18 dan `026` TC-GS-PROFILE-151 langkah 17-20; berlaku sama untuk spec lain yang mengklik area di luar popup form.
- **Spec meminta:** klik di luar popup Change Password membuat popup tetap terbuka, baik form kosong (150) maupun sudah terisi (151), tanpa dialog Unsaved Changes (151 langkah 20).
- **Kenyataannya:** DialogForm menutup popup yang belum diubah saat area di luar diklik, seperti default mayoritas design system (MUI Dialog, Chakra Modal, Mantine Modal, antd Modal). Bila form sudah diubah, popup tetap terbuka dan dialog Unsaved Changes muncul agar isian tidak hilang tanpa konfirmasi.
- **Keputusan:** perilaku komponen menang. 150: klik backdrop menutup popup; langkah yang memakai popup "yang masih terbuka" membukanya lagi lewat [Change Password]. 151: klik backdrop memunculkan Unsaved Changes dan popup tetap terbuka; langkah 20 mengasersi dialog itu muncul, lalu memilih kembali ke form.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (perilaku komponen di atas spec, 2026-11-08), 2026-11-14.
- **Diterapkan di:** MyProfile 025, 026.
- **Sumber:** wangs-ui DialogForm (`clickBackdrop`, behavior catalog TC-6496).

## D-197 Setelah login, tujuan pertama selalu Portal — Product Hub, juga saat membuka URL halaman dalam tanpa sesi (2026-11-14)

- **Spec / langkah:** GlobalSettings/MyProfile `015` TC-GS-PROFILE-71 langkah 8-10. Berlaku sama untuk spec lain yang membuka URL halaman dalam tanpa sesi lalu mengharapkan kembali ke halaman itu setelah login.
- **Spec meminta:** tanpa sesi aktif, membuka URL My Profile diarahkan ke Login, dan setelah login (Pre-setup #1, jalur MFA Authenticator) kembali ke My Profile.
- **Kenyataannya:**
  - PRD login-password L907, kontrak `auth-foundation.md` §7a: tujuan redirect login sukses "selalu ke Portal dulu (semua entitas)". L157, L632 dan L915 juga menyebut redirect ke Portal — Product Hub.
  - PRD MFA §11 (tc-mfa L549, TC-AUTH-MFA-178): Product Hub adalah tujuan redirect setelah MFA.
  - Backend menjawab verify MFA dengan `redirectTo: "/portal/product-hub"`, dan app mengikutinya.
  - Tidak ada baris PRD tentang kembali ke halaman yang dituju setelah login; hanya test case yang memintanya.
- **Keputusan:**
  - PRD menang: app sudah benar.
  - Langkah 10 mengasersi halaman Portal — Product Hub setelah login. Lalu My Profile dibuka dari Portal (atau lewat URL-nya) dan diasersi tampil untuk user itu.
  - Bukan ui-gap, dan tidak ada perbaikan app.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner (PRD sebagai acuan), 2026-11-14.
- **Diterapkan di:** MyProfile 015.
- **Sumber:** PRD auth login-password L157, L632, L907, L915; PRD MFA §11.

## D-198 Langkah multi-tab dengan SSE dibatasi batas koneksi per host lingkungan e2e (HTTP/1.1) (2026-11-14)

- **Spec / langkah:** GlobalSettings/Import `175` TC-GS-IMPORT-542, langkah yang membuka tab ke-6 dan ke-7. Berlaku sama untuk spec lain yang membuka banyak tab sekaligus, dengan tiap tab memegang koneksi SSE.
- **Spec meminta:** tujuh tab import terbuka bersamaan, masing-masing dengan sesi aktif.
- **Kenyataannya:**
  - Stack e2e melayani app lewat HTTP/1.1 (network-resources run Imp175, 2.417 record h1).
  - Chrome membatasi 6 koneksi bersamaan per host. Tiap tab memegang 2 SSE, jadi di tab ke-6 request baru (GET validate, POST product-sessions) tertahan di browser dan tidak pernah sampai ke server.
  - Request yang sama lewat nama host lain dijawab dalam 7 ms. Backend tidak bermasalah, dan produksi di balik HTTP/2 tidak terkena batas ini.
- **Keputusan:**
  - **Kalau tab-tab itu membangun sesi bersamaan untuk menguji batas atau konflik:** sesi tab sebelumnya dibuat lewat helper API (POST product-sessions dan validate) dengan user yang sama. Ini sama dengan tab lain milik user itu, atau perangkat lain. Cukup 2-3 tab UI asli, dan reaksi UI diasersi di tab terakhir.
  - **Kalau tiap tab mengasersi UI-nya sendiri:** tab ditutup setelah asersinya selesai, sehingga paling banyak 3 tab ber-SSE terbuka.
  - Bukan gap BE dan bukan ui-gap.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14.
- **Diterapkan di:** Import 175.
- **Sumber:** run Tri-mac-20261114-1619 dan Imp175brk (spectra inspect eval), plans/global-settings-import/integration-findings.md baris 67.

## D-199 Save tanpa perubahan di Edit Subscription: yang diasersi adalah tidak ada write di server, bukan tidak ada request (2026-11-14)

- **Spec / langkah:** AdminConsole/ClientSubscription `118` TC-231 / TC-458 langkah 11.
- **Spec meminta:** Save tanpa perubahan tidak mengirim request mutasi.
- **Kenyataannya:**
  - Aplikasi mengirim `PATCH /subscriptions/{id}` `{durationYears, startDate}`.
  - Kontrak menjawab edit tanpa perubahan dengan `204`. FE memetakan `204` ke `unchanged`, lalu menampilkan "No changes to save." dengan dialog tetap terbuka (decisions.md aplikasi L275).
  - Tidak ada baris Changelog, Activity Log, atau System Log yang ditulis.
- **Karena:** kontrak sengaja menyediakan jawaban `204` untuk edit yang tidak mengubah apa pun, jadi request ke server adalah perilaku yang dikontrakkan. Yang diminta spec, yaitu data tidak berubah, tetap bisa diamati.
- **Keputusan:**
  - Langkah 11 mengasersi:
    - `PATCH` dijawab `204`;
    - pesan "No changes to save.";
    - dialog tetap terbuka;
    - tidak ada baris log baru.
  - Tidak ada asersi "tidak ada request". Ini bukan ui-gap.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (temuan Integration B).
- **Diterapkan di:** ClientSubscription 118.
- **Sumber:** run CS-unwrap-win-20261114-bb; decisions.md aplikasi L275.

## D-200 Nilai tanggal di baris Changelog Edit Subscription: diasersi tanggal kalendernya, bukan format glyph (2026-11-14)

- **Spec / langkah:** AdminConsole/ClientSubscription `120` TC-461, dan TC-459 langkah 139-140.
- **Spec meminta:** Old/New value Start Date di baris Changelog memakai format tanggal tenant `dd/MM/yy` (misalnya `15/11/26`).
- **Kenyataannya:**
  - Stack menulis `15 Nov 2026` → `14 Nov 2026` (`d MMM yyyy`). Teks ini ditulis backend ke log, tidak diformat oleh FE.
  - PRD §8.1 L1485 hanya menyebut `[Old Start Date] → [New Start Date]`, tanpa format.
  - LLD license-allocation-subscription (Edit, L870-L888) hanya memberi contoh Duration (`1 year(s)` → `2 year(s)`). Satu-satunya aturan tanggal di LLD (L114, L705) adalah serialisasi field API `YYYY-MM-DDT00:00:00Z`, bukan teks log.
- **Karena:** PRD dan LLD sama-sama tidak menetapkan format teks tanggal di log. Format glyph termasuk presentasi (D-096), sedangkan tanggal mana yang tercatat adalah data yang harus benar.
- **Keputusan:**
  - Nilai Old/New diasersi sebagai tanggal kalender. Nilai diterima bila terbaca sebagai hari yang sama, dalam format `dd/MM/yy` atau `d MMM yyyy`.
  - Format glyph tidak diasersi.
  - Celah dokumen ini diajukan sebagai issue ke pemilik LLD supaya format nilai log ditetapkan.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (temuan Integration B).
- **Diterapkan di:** ClientSubscription 120.
- **Sumber:** run CS-unwrap-win-20261114-bb; PRD §8.1 L1484-L1485; LLD license-allocation-subscription L114, L705, L870-L888.

## D-201 Code yang bentrok lagi saat retry otomatis di Create Division keluar dari e2e dan dijaga test backend (2026-11-14)

- **Spec / langkah:** GlobalSettings/Division `022` (TC-GS-DIV-E2E-022) TC-GS-DIV-80, langkah 42-63.
- **Spec meminta:**
  - Admin kedua membuat `Quality Rival {runId}-022` dengan Code `QRT2`, tepat di antara percobaan Create pertama Session A dan retry Code otomatis oleh server.
  - Create Session A lalu mendapat Code berikutnya. Retry yang bentrok lagi diperlakukan sebagai kegagalan biasa.
- **Kenyataannya:**
  - Konflik dan retry terjadi di dalam satu request server.
  - Tidak ada fault hook atau test route yang bisa menaruh Division di jendela itu.
  - Intercept tidak boleh memalsukan jawaban server.
- **Karena:** state itu butuh timing presisi di dalam satu request backend, dan e2e hanya membangun state lewat cara yang benar-benar terjadi. Tingkat service/repository bisa mengujinya lewat test unit atau integrasi backend, e2e tidak.
- **Keputusan:**
  - Langkah 42-63 keluar dari e2e, sebagai cacat spec untuk lapisan e2e. Perilakunya dijaga test backend.
  - TC-GS-DIV-272, TC-GS-DIV-273 dan TC-GS-DIV-79 tetap di e2e.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (usulan Integration B 2026-11-10, diajukan ulang Integration C).
- **Diterapkan di:** Division 022.
- **Sumber:** global-settings/division/TestCases/tc-division.md (TC-GS-DIV-80); aturan Code auto-generate di PRD Division; repo aplikasi plans/global-settings-user/integration-findings.md L1724-L1733.

## D-202 Kunci TAG di plan dasar (AllTags) diskip sebagai contract drift: `/me/entity` tidak membawa Pricing Type atau rank (2026-11-14)

- **Spec / langkah:** GlobalSettings/AllTags `010` dan `011`, langkah kunci TAG per plan (TAG-LOGIC-08).
- **Spec meminta:** di plan dasar, semua tipe TAG selain QR terkunci.
- **Kenyataannya:**
  - PRD All TAGs §9.10 (TAG-LOGIC-08) dan Plans & Features PRD §4.1.3 L418 serta §9.2 L1331 (baris "TAG Features") menurunkan akses TAG dari Pricing Type plan: rank 0 berarti QR saja (plans.md L21/L30/L41/L47). PRD tidak punya baris katalog fitur untuk kunci ini.
  - Kontrak `GET /v2/me/entity` (auth me/API/low-level-design.md L135 dan L192, openapi MeEntity, PR #18) hanya membawa `plan: {name, features}`, tanpa rank dan tanpa pricingType.
  - Contoh baris `fixed_asset_module/tag_activation/unlimited` di openapi tidak ada di katalog PRD.
- **Karena:** sinyal yang dibutuhkan PRD tidak ada di kontrak. Mencocokkan `plan.name` dengan "Free" atau "Starter" adalah tebakan yang rusak begitu plan default diganti namanya. Aturan owner (2026-11-08): drift diskip, tanpa improvisasi. Prinsip owner 2026-11-07: kondisi dibaca dari plan, bukan dari free atau paid.
- **Keputusan:**
  - Langkah kunci TAG per plan di 010/011 diskip sebagai contract drift.
  - FE tidak memakai pencocokan nama plan. Perilaku layar TAG saat ini tetap, dan server tetap menolak write yang terkunci (TAG-LOGIC-08c).
  - Drift ini diajukan sebagai issue ke pemilik kontrak `/me/entity`: Pricing Type atau rank, atau baris fitur akses TAG, belum ada di payload plan.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (temuan Integration B).
- **Diterapkan di:** AllTags 010, 011.
- **Sumber:** PRD All TAGs §9.10; Plans & Features PRD §4.1.3 L418, §9.2 L1331; plans.md L21/L30/L41/L47; auth me/API/low-level-design.md L135, L192; openapi MeEntity.

## D-203 Kandidat popup Assign User to Role (Global Role) untuk aktor Total Control: pemegang Read Only diskip sebagai contract drift (2026-11-14) (ditarik oleh D-204)

- **Spec / langkah:** AdminConsole/SettingsRolePermission `045` langkah 10 dan 22 (picker assignment Manage language).
- **Spec meminta:** kandidat tidak memuat pemegang role, yaitu seluruh Total Control dan Read Only, Default User, dan aktor sendiri. Search `Anggraini` (pemegang Read Only Dewi Anggraini) menampilkan `No results found`.
- **Kenyataannya:**
  - PRD settings-role-permission §9.5 (baris "Popup Assign User ke Role — Global Role") mengecualikan user yang sudah punya penugasan pada Global Role ini, Default User, Total Control, dan aktor sendiri.
  - Pemegang Read Only memegang setiap Global Role lewat pola tingkat akses (§2.3; cascade `Assign (via Read Only)` di §8.3 dan §8.4). Menurut PRD, mereka termasuk user yang sudah punya penugasan.
  - LLD assignable-users.md L23-L24 menetapkan pengecualian per picker tanpa menyebut bahwa `excludeKey` mengecualikan pemegang Read Only. Kode stack (assignable_users_query_builder.go L193-L199) sengaja tetap menampilkan pemegang Read Only untuk aktor Total Control, karena baris pola tier tidak dihitung sebagai pemegang `excludeKey`.
- **Karena:** PRD dan LLD/stack berbeda soal apakah penugasan lewat pola Read Only dihitung sebagai "sudah punya penugasan". Aturan owner (2026-11-08): drift diskip tanpa improvisasi dan diajukan sebagai issue.
- **Keputusan:**
  - Langkah 10 (bagian pemegang Read Only) dan langkah 22 diskip sebagai contract drift.
  - Pengecualian lain di langkah 10 (pemegang langsung, Total Control, Default User, aktor) tetap diasersi.
  - Drift ini diajukan sebagai issue ke pemilik LLD assignable-users.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (temuan Integration B).
- **Diterapkan di:** SettingsRolePermission 045.
- **Sumber:** PRD admin-console/settings-role-permission §9.5, §2.3, §8.3, §8.4; LLD assignable-users.md L23-L24; iam assignable_users_query_builder.go L193-L199.

## D-204 Kandidat popup Assign User to Role (Global Role) untuk aktor Total Control memuat pemegang Read Only; menarik D-203 (2026-11-14)

- **Spec / langkah:** AdminConsole/SettingsRolePermission `045`, langkah 10 (TC-AC-RP-161, aktor Total Control Siti Nurhaliza) dan langkah 22 (pool aktor "Manage user and role", aktor diganti di langkah 12).
- **Spec meminta:** di langkah 10, kandidat tidak memuat seluruh Total Control dan Read Only.
- **Kenyataannya:**
  - PRD settings-role-permission §9.5 L2514 mengecualikan user yang sudah punya penugasan pada Global Role ini, Default User, Total Control, dan aktor sendiri. PRD lalu menambahkan: "Bagi aktor 'Manage user and role': exclude juga target Read Only."
  - Karena pengecualian Read Only hanya disebut untuk aktor "Manage user and role", pool aktor Total Control memuat pemegang Read Only.
  - LLD assignable-users.md L24 menyatakan hal yang sama ("A Total Control actor's Global Role pool includes Read Only holders"), dan stack mengikutinya.
- **Karena:** PRD, LLD, dan kode sepakat. Bacaan D-203 (pemegang Read Only dianggap sudah punya penugasan lewat pola tier) tidak didukung §9.5, sehingga ini kesalahan spec, bukan contract drift.
- **Keputusan:**
  - Langkah 10 mengasersi bahwa Total Control, Default User, aktor, dan pemegang langsung tidak muncul, sedangkan pemegang Read Only muncul.
  - Langkah 22 tetap seperti tertulis, karena di pool aktor "Manage user and role" pemegang Read Only memang dikecualikan.
  - D-203 ditarik.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (koreksi Integration B).
- **Diterapkan di:** SettingsRolePermission 045.
- **Sumber:** PRD admin-console/settings-role-permission §9.5 L2514; LLD assignable-users.md L24; iam assignable_users_query_builder.go L193-L199.

## D-205 Pemisah tanggal dan jam pada nilai Date Time tampilan tidak diasersi; nilai tanggal, jam, dan zona waktunya diasersi (2026-11-14)

- **Spec / langkah:** FixedAsset/SettingsChartOfAccounts `TC-FA-FACO-UI-120` (kolom Last Updated, spec.md baris 43, 144-146), dan setiap spec lain yang menulis Date Time tampilan dengan koma, misalnya `25/03/26, 09:15`.
- **Spec meminta:** Last Updated tampil `25/03/26, 09:15`, dengan koma setelah tanggal, pada K1 Date Format `dd/MM/yy`, Time Format 24h, Time Zone UTC.
- **Kenyataannya:**
  - Aplikasi menampilkan `25/03/26 09:15`, tanpa koma, lewat preset date Wangs UI yang mengikuti General Settings.
  - General Settings PRD §4.3b mendefinisikan pratinjau format sebagai `17/03/23 14:30` (L310, L490), tanpa koma.
  - Contoh tabel di PRD yang sama (L273-L277) dan prd-conventions §Date/DateTime memakai koma, tetapi konvensi menyatakan contoh semacam itu ilustratif ("contoh, bukan format tetap").
- **Karena:** PRD tidak konsisten soal pemisah. Glyph pemisah termasuk presentasi (D-096), sedangkan tanggal, jam, dan zona waktu yang tampil adalah data yang harus benar.
- **Keputusan:**
  - Nilai diasersi per tanggal dan jam sesuai Date Format, Time Format, dan Time Zone General Settings.
  - Pemisah di antara tanggal dan jam (spasi atau `, `) tidak diasersi.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (temuan sesi slicing, component test Chart of Accounts).
- **Diterapkan di:** SettingsChartOfAccounts 120; component test slicing Chart of Accounts.
- **Sumber:** PRD global-settings/general-settings §4.3b L273-L277, L310, L490; foundation prd-conventions §Date/DateTime (aturan wajib Date/DateTime, contoh ilustratif).

## D-206 Switch Active Admin Console untuk user yang nonaktif di Global Settings tampil Off dan disabled (2026-11-14)

- **Spec / langkah:** AdminConsole/SettingsUser 020 `TC-AC-SU-100` langkah 14-15, bertentangan dengan 174 `TC-AC-SU-598` langkah 4.
- **Spec meminta:**
  - 020 menyatakan switch Active Admin Console tetap On (posisi terakhir), disabled, dengan tooltip.
  - 174 menyatakan switch pada keadaan yang sama tampil Off.
- **Kenyataannya:**
  - Aplikasi menampilkan Off, disabled, dengan tooltip yang benar (`isActive && isActiveGlobal`, perbaikan F-INT-SU-12 2026-11-10).
  - API users/list mengembalikan `isActive: true, isActiveGlobal: false` untuk user tersebut.
- **Karena:** PRD ACSU-LOGIC-09 menetapkan status aktif sebagai AND dari status Admin Console dan Global Settings, dan dokumen API user-actions.md L29 sejalan. 174 mengikuti aturan ini, sedangkan 020 tidak.
- **Keputusan:**
  - 020 langkah 14-15 mengasersi switch Off dan disabled, dengan tooltip.
  - Aplikasi tidak diubah.
- **Diputuskan oleh:** Wangs-UI Coordinator atas nama owner, 2026-11-14 (temuan Integration C).
- **Diterapkan di:** SettingsUser 020.
- **Sumber:** PRD admin-console/settings-user ACSU-LOGIC-09; API doc user-actions.md L29; SettingsUser 174 `TC-AC-SU-598` langkah 4.
