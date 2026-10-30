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
