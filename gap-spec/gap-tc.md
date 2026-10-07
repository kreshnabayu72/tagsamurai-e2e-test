# Gap & Temuan — Auth > Login with Password

Sumber: generate spec `specs/auth2/LoginPassword/` (20 spec, 74 TC aktif). Tanggal generate: 2026-10-05.

Dokumen ini hanya berisi temuan yang muncul **selama proses generate spec**. Ini bukan hasil audit PRD/TC menyeluruh, dan bukan pemrosesan gap registry. Temuan dari sumber lain yang sudah tercatat di `foundation/prd-gap-registry.md` tidak diulang di sini kecuali yang merujuk langsung ke spec yang baru dibuat.

---

## GAP-LP-E2E-001 — Konflik copy antara PRD dan Test Case pada layar Confirm to Continue

**Status:** terbuka
**Tipe:** inkonsistensi PRD vs TC vs file TC FE
**Dampak:** median, hanya teks

PRD `login-password.md` §4.5 dan §10 mendefinisikan copy layar Confirm to Continue sebagai:

- Label checkbox: `"I have read and agree to the Terms of Service and Privacy Policy"`
- Tombol: `[Continue to Dashboard ➔]`

`TC-AUTH-LP-90` menuliskan copy yang berbeda:

- Label checkbox: `"I agree to the Privacy Policy"`
- Tombol: `"Continue"`

File `tc-login-password-frontend.md` mengulang copy yang sama dengan TC di `TC-AUTH-LP-FE-10` step 2. Jadi ini bukan salah ketik satu tempat saja, melainkan copy versi TC sudah ikut turun ke dokumen turunan, dan ketiganya masih dipakai bersama.

**Yang dipakai spec:** copy dari PRD. Alasan: PRD adalah source of truth untuk UI, dan spec e2e menguji perilaku, bukan ketepatan ejaan tombol.

**Yang perlu diputuskan:** salah satu dari sumber harus diubah supaya tidak ada dua copy yang sama-sama benar.
- Opsi A: koreksi `TC-AUTH-LP-90` dan `TC-AUTH-LP-FE-10` agar mengikuti PRD.
- Opsi B: koreksi PRD §4.5 dan §10 bila copy yang dipakai produk adalah versi TC.

**Verifikasi awal:** `TC-AUTH-LP-19`, `21`, dan `22` di spec `TC-AUTH-LP-E2E-012` serta langkah 5 dan 21 di spec `TC-AUTH-LP-E2E-013` memakai copy PRD. Kalau keputusan diambil ke Opsi B, baris-baris itu perlu diperbarui.

---

## GAP-LP-E2E-002 — Changelog menyatakan web-only, tetapi tiga TC mobile masih ada

**Status:** terbuka
**Tipe:** inkonsistensi internal file TC
**Dampak:** tinggi untuk keputusan cakup automation

Changelog `tc-login-password.md` entri **2026-10-01** menyatakan:

> Mobile removal (web-only) — 3 TC dicabut, ID dipertahankan (tidak dinomori ulang), total 77→74. TC layout mobile/responsive dicabut sesuai konvensi `testcase-conventions.md` (**file TC hanya mencakup skenario web**). Dicabut: `TC-AUTH-LP-82`, `TC-AUTH-LP-83`, `TC-AUTH-LP-84`.

Namun tiga TC mobile masih ada di file yang sama dan tidak dicabut:

| TC | Judul | Sifat |
|---|---|---|
| `TC-AUTH-LP-2` | Buka halaman Login with Password (Mobile app) — default | Mobile only, tidak ada padan web |
| `TC-AUTH-LP-17` | Mobile app — tidak ada widget & tidak divalidasi | Mobile only, berbeda aturan dari web |
| `TC-AUTH-LP-45` | Lock per-platform independen (web ≠ mobile) | Menyentuh dua platform sekaligus |

Tiga TC ini **tidak bisa dihapus** dengan alasan yang sama seperti 82–84, karena 82–84 adalah skenario layout mobile yang memang punya padan web, sedangkan ketiganya menguji aturan yang benar-benar berbeda antar platform. Aturan pada changelog itu sendiri juga menyebut "TC khusus mobile dipertahankan bila fitur hanya ada di mobile atau aturannya berbeda dari web".

**Yang perlu diputuskan:** perjelas apakah file TC adalah web-only dengan pengecualian, atau memang mencakup mobile pada kasus khusus. Keputusan ini menentukan apakah spec 019 dan 020 tetap ada di suite ini.

**Sementara ini:** spec 019 dan 020 tetap dibuat dan memakai `coverage.mobile`, karena ketiganya menguji perilaku yang benar-benar berbeda antar platform. Kalau disepakati file TC web-only, ketiga TC ini perlu dipindah ke file TC mobile, bukan dihapus.

---

## GAP-LP-E2E-003 — `TC-AUTH-LP-2` merujuk §2.6 yang sudah tidak ada di PRD

**Status:** terbuka
**Tipe:** referensi rusak
**Dampak:** rendah

`TC-AUTH-LP-2` menuliskan subtitle mobile sebagai `(sama pola web, §2.6)`.

Pada PRD `login-password.md` versi sekarang, section 2 hanya punya satu sub-section, yaitu `### 2.1 UI Visibility per State`. Tidak ada §2.6.

Rujukan §4.9 pada TC yang sama **masih valid** karena `### 4.9 Mobile Layout Spec` masih ada di PRD. Yang rusak hanya bagian §2.6.

**Kemungkinan penyebab:** PRD pernah punya struktur §2.x yang lebih rinci sebelum digabung ke single-file, dan nomor section tidak diperbarui saat digabung.

**Yang perlu dilakukan:** perbarui rujukan di `TC-AUTH-LP-2` menjadi §4.9 Mobile Layout Spec, atau tambahkan sub-section §2.6 bila informasinya memang masih relevan.

---

## GAP-LP-E2E-004 — Threshold IP rate limit belum ditetapkan

**Status:** terbuka, sudah ada di sumber
**Tipe:** `[TODO Engineering]`
**Dampak:** tinggi, membuat spec 016 belum bisa punya angka ekspektasi final

PRD `login-password.md` §9.2 masih menandai threshold IP rate limiting sebagai `[TODO Engineering]`. `tc-login-password.md` §Catatan juga menyebutkan bahwa `TC-AUTH-LP-63` dipelihara sebagai gap terbuka, bukan gap baru.

**Yang sudah dilakukan di spec:** `TC-AUTH-LP-E2E-016` menjalankan request berulang dari IP yang sama sampai status `429` dan caption "Too many requests. Please try again later." muncul, lalu **mencatat jumlah request yang dibutuhkan** sebagai bahan konfirmasi threshold. Jadi spec ini sudah runnable dan menghasilkan angka, tetapi tidak bisa mengasumsikan angka final.

**Yang perlu ditetapkan:** nilai threshold per window, dan window-nya. Setelah ditetapkan, spec 016 bisa menambahkan assert jumlah request yang pasti.

---

## GAP-LP-E2E-005 — Target environment e2e belum diarahkan

**Status:** terbuka, di luar cakupan dokumen Auth
**Tipe:** kekosongan environment
**Dampak:** memblokir eksekusi, bukan pembuatan spec

`tagsamurai-e2e-test/spectra.config.ts` masih menunjuk demo app bawaan TestSpectra. PRD `login-password.md` tidak menetapkan target environment e2e.

**Dampak:** semua 20 spec di suite ini belum bisa dijalankan sampai `spectra.config.ts` diarahkan ke environment yang benar. Ini dicatat di `Prerequisites` spec 002 dan tidak menjadi alasan mengeluarkan TC.

---

## GAP-LP-E2E-006 — Kebutuhan environment belum tersedia untuk enabled spec

**Status:** terbuka, sudah dicatat di Prerequisites tiap spec
**Tipe:** kekosongan environment
**Dampak:** memblokir eksekusi spec tertentu, bukan pembuatan spec

Semua kebutuhan berikut dicatat di `Prerequisites` sebagai sumber resmi bagi tim FE:

| Kebutuhan | Spec yang membutuhkan |
|---|---|
| Mailbox uji untuk email reset password | 008, 011, 012 |
| Pemicu waktu untuk melewati window lock | 005, 006, 007 |
| Pemicu pergantian `attempt_date` ke hari berikutnya | 007 |
| Token confirm-agreement dengan TTL pendek | 013 |
| Device dan geolokasi yang sudah tercatat pada user | 002, 014 |
| Pre-auth device token yang dibuat lewat API admin | 014 |
| Konteks browser kedua untuk skenario dua perangkat | 002, 020 |
| Device atau emulator mobile dengan viewport di bawah 768px | 019, 020 |
| Intercept pada endpoint `POST /auth/login` | 016, 017 |
| Intercept pada jalur server ke provider reCAPTCHA | 010 |
| Kemampuan mengosongkan counter rate limit per IP | 016 |

Sesuai `docs/e2e-conventions.md` bagian 2, tidak satu pun dari kebutuhan ini dipakai sebagai alasan mengeluarkan TC.

---

## GAP-LP-E2E-007 — `tc-login-password-frontend.md` stale, tiga TC automatizable belum masuk

**Status:** terbuka
**Tipe:** dokumen turunan tidak sinkron dengan file TC utama
**Dampak:** sedang, hanya consistency dokumen

Audit silang `tc-login-password-frontend.md` terhadap `tc-login-password.md` menunjukkan 5 TC yang ada di file TC utama tapi tidak dirujuk di file FE:

| TC | Sifat di file TC utama | Alasan tidak ada di file FE |
|---|---|---|
| `TC-AUTH-LP-63` | `Manual Only`, threshold IP rate limit | File FE meng-exclude `Manual Only` lewat Aturan #5 miliknya sendiri |
| `TC-AUTH-LP-88` | `Manual Only`, validasi 120 karakter pada form Register | Sama seperti di atas |
| `TC-AUTH-LP-92` | Automatable, submit lintas beberapa tab | Ditambahkan setelah snapshot file FE |
| `TC-AUTH-LP-93` | Automatable, `#93`, pengosongan Password | Ditambahkan setelah snapshot file FE |
| `TC-AUTH-LP-94` | Automatable, `#94`, device/browser canonical | Ditambahkan setelah snapshot file FE |

Header file FE masih menuliskan cakupan sampai `TC-AUTH-LP-91`, padahal `93` masuk lewat changelog 2026-09-14 dan `94` lewat 2026-09-18.Angka ringkasan di file FE juga masih memakai hitungan lama.

**Keputusan yang sudah diambil:** kelima TC tetap masuk spec, dan spec tidak chasing file FE.
- Alasannya dua. Pertama, `docs/e2e-conventions.md` bagian 2 menyatakan label `Manual Only` bukan alasan mengeluarkan TC, jadi aturan #5 di file FE bertentangan dengan konvensi repo. Kedua, `TC-AUTH-LP-92` sampai `94` memang `Automatable`, jadi mengeluarkan ketiganya hanya karena file FE belum diperbarui akan menjadi coverage gap yang disengaja.

**Verifikasi awal:** seluruh 69 TC yang dirujuk file FE sudah ada di spec. Tidak ada TC FE yang terlewat. Spec 005 dan 013 sudah menerima `92`, spec 001 sudah menerima `93`, dan spec 003 sudah menerima `94`.

**Yang perlu dilakukan:** perbarui `tc-login-password-frontend.md` supaya sinkron dengan `tc-login-password.md`, dan samakan aturan `Manual Only` di file FE dengan `docs/e2e-conventions.md` bagian 2.

---

## GAP-LP-E2E-008 — `TC-AUTH-LP-FE-10` salah soal status tombol Continue

**Status:** terbuka
**Tipe:** inkonsistensi file TC FE vs PRD vs file TC utama
**Dampak:** sedang, karena menyesatkan implementasi dan pengujian

PRD `login-password.md` §4.5 menuliskan tombol footer secara eksplisit:

> Button [Continue to Dashboard ➔] (`variant="solid"`, `severity="primary"`, `className="w-full"`, **enabled — validasi client-side saat klik**)

`TC-AUTH-LP-19` dan `TC-AUTH-LP-90` di file TC utama juga menyebut tombol itu **enabled**, dengan validasi baru berjalan saat diklik.

`TC-AUTH-LP-FE-10` step 2 di file FE menuliskan sebaliknya: tombol Continue **disabled sampai checkbox dicentang**. Dua sumber lain tidak menyebut status itu sama sekali.

**Yang dipakai spec:** status **enabled**. Spec 012 memverifikasi tombol dalam keadaan enabled sebelum checkbox dicentang, lalu memverifikasi caption error muncul setelah diklik tanpa centang.

**Yang perlu dilakukan:** koreksi `TC-AUTH-LP-FE-10` step 2. Kalau ternyata desain memang memakai tombol disabled sampai dicentang, PRD §4.5 dan `TC-AUTH-LP-19` justru yang perlu diubah, dan spec 012 harus ditulis ulang.

---

## GAP-LP-E2E-009 — Post condition `TC-AUTH-LP-26` lebih lemah dari PRD

**Status:** terbuka
**Tipe:** inkonsistensi file TC utama vs PRD
**Dampak:** rendah, hanya memengaruhi cakupan assert

PRD `login-password.md` §9.2 menyatakan bahwa user yang tidak mengonfirmasi, baik karena menutup layar maupun karena `preAuthToken` expired tanpa dipakai, sama-sama menghasilkan `Failed` + Note `Consent not given`. PRD §11.4 juga menandai kombinasi itu dengan `✅` pada kolom "Tercatat di User Log".

`TC-AUTH-LP-26` menuliskan post condition yang lebih lemah:

> Login dibatalkan; dicatat `Consent not given` bila terdeteksi sbg abandoned

Frasa "bila terdeteksi sbg abandoned" membuat pencatatan ini terasa opsional, padahal untuk kasus token kedaluwarsa mekanismenya sudah pasti: user sudah melewati password benar, sudah mencentang, lalu klik Continue.

**Yang dipakai spec:** spec 013 memakai versi PRD dan menguji assert `Consent not given` pada kedua kasus, penutupan layar maupun token kedaluwarsa. Kalau ternyata server memang tidak menulis entri untuk kasus kedaluwarsa, spec 013 perlu dilonggarkan dan PRD §11.4 perlu dikoreksi.

---

## Kepatuhan

- Tidak ada TC aktif yang dikeluarkan dari spec. 74 dari 74 tercakup, tanpa duplikasi `sourceTc`.
- 20 TC yang tidak punya spec dicabut dari file TC sebelum generate ini, bukan dibuang oleh proses spec. Rinciannya ada di `docs/coverage/AuthLoginPassword.md`.
- Audit silang terhadap `tc-login-password-frontend.md` menemukan 8 ketidaksesuaian expected-result, semuanya sudah dikoreksi di spec. Lihat bagian "Hasil audit silang terhadap `tc-login-password-frontend.md`" di `docs/coverage/AuthLoginPassword.md`.
- Dua gap tertutup lewat keputusan, bukan lewat koreksi dokumen sumber:
  - `GAP-LP-E2E-001` copy layar Confirm to Continue. Spec memakai copy PRD. Sumbernya masih perlu diseragamkan oleh pemilik dokumen.
  - `GAP-LP-E2E-007` cakupan `tc-login-password-frontend.md`. Spec memakai `tc-login-password.md` sebagai source of truth, sesuai `docs/e2e-conventions.md` bagian 2.
- Status seluruh spec `draft`; belum ada `.test.ts`.
- `npx spectra lint --strict specs/auth2/LoginPassword` → `✓ 20 specs and 1 suites verified. 0 lint errors found.`
- Scan residue CJK dan full-width pada 20 spec plus dua dokumen pendukung: `0 baris`.


---

# Gap & Temuan — Auth > Login with OTP

Sumber: generate spec `specs/Auth/LoginOtp/` (27 spec, 183 TC aktif). Tanggal generate: 2026-10-06.

Dokumen ini mencatat seluruh temuan, perbedaan langkah/prekondisi, dan celah cakupan yang diidentifikasi selama proses **audit silang antara PRD `auth/login-otp/PRD/login-otp.md` dan Test Case `auth/login-otp/TestCases/tc-login-otp.md`**.

---

## GAP-OTP-E2E-001 — Nilai threshold IP Rate Limit belum ditetapkan secara kuantitatif

**Status:** terbuka, bawaan PRD  
**Tipe:** `[TODO Engineering]`  
**Dampak:** tinggi untuk penentuan batas ekspektasi assert otomasi non-mock  

PRD `login-otp.md` §9.2 dan `auth-foundation.md` §3.2 menandai threshold IP rate limiting sebagai `[TODO Engineering]`. Di sisi lain, `TC-AUTH-OTP-33`, `TC-AUTH-OTP-34`, `TC-AUTH-OTP-63`, dan `TC-AUTH-OTP-85` menguji perilaku penolakan saat rate limit tercapai (status `429` dan alert inline "Too many requests. Please try again later."), namun jumlah request spesifik per time-window tidak disebutkan di dokumen TC maupun PRD.

**Yang dilakukan di spec:**  
`TC-AUTH-OTP-E2E-008` menjalankan pengujian menggunakan skenario mock/threshold trigger yang memicu status 429 dan memverifikasi perilaku UI:
1. Alert inline tampil di atas button [Request OTP].
2. Penggantian alamat email pada IP yang sama tetap terblokir.
3. Nilai 6 digit di kotak verifikasi tidak dikosongkan (NC-10).
4. Penolakan tercatat di Activity Log Session dengan Note `IP rate limit exceeded`.

**Yang perlu diputuskan tim Engineering:**  
Menetapkan angka batas request per window (misal: 10 request per 60 detik per IP) agar skenario uji otomasi end-to-end tanpa mock dapat melakukan perulangan request dengan hitungan batas yang pasti.

---

## GAP-OTP-E2E-002 — Ketiadaan Skenario Attestation Token Negatif / Kedaluwarsa pada TC Mobile

**Status:** terbuka  
**Tipe:** kelengkapan skenario uji / precondition  
**Dampak:** sedang, memengaruhi cakupan pengujian aplikasi mobile  

PRD `login-otp.md` §4.6 dan §9.2 menetapkan bahwa aplikasi mobile tidak merender widget Google reCAPTCHA v2, melainkan menggunakan mekanisme native device attestation (Google Play Integrity API) untuk memvalidasi keaslian perangkat klien sebelum OTP dikirimkan.

File TC hanya menyediakan satu pengujian attestation pada `TC-AUTH-OTP-180` yang menguji skenario positif (token attestation valid). Skenario negatif belum tercakup di file TC:
1. Perangkat gagal verifikasi integritas (device rooted / uncertified).
2. Attestation token kadaluwarsa atau null.
3. Pesan kesalahan yang ditampilkan antarmuka mobile saat attestation gagal (apakah alert modal, toast, atau penolakan server).

**Yang dilakukan di spec:**  
`TC-AUTH-OTP-E2E-002` mencakup alur tampilan mobile tanpa reCAPTCHA, keypad numerik otomatis, dan permintaan OTP dengan attestation token valid. Ketiadaan skenario negatif dicatat di sini sebagai rekomendasi penambahan TC ke suite mobile.

---

## GAP-OTP-E2E-003 — Inkonsistensi Microcopy Error Caption Checkbox Agreement Antar Modul Auth

**Status:** terbuka  
**Tipe:** inkonsistensi copy antar dokumen PRD & TC  
**Dampak:** rendah hingga sedang, memengaruhi validasi string pesan kesalahan  

Terdapat perbedaan teks pesan kesalahan inline saat pengguna mengklik tombol [Continue ➔] pada layar Confirm to Continue tanpa mencentang checkbox privasi:

- **Modul Login with Password (`login-password.md` §4.5 & `auth-foundation.md` §11.1):**  
  Menggunakan copy: `"Please agree to the Privacy Policy to continue"`
- **Modul Login with OTP (`login-otp.md` §4.2, §6 V-12, §9.9 FLD-06 serta `TC-AUTH-OTP-102`):**  
  Menggunakan copy: `"You need to agree to the Privacy Policy to continue"`

Keduanya merujuk pada layar dan komponen yang sama ("Confirm to Continue" / Agreement Gate).

**Yang dipakai di spec:**  
Spec `TC-AUTH-OTP-E2E-021` mengadopsi copy resmi dari PRD Login with OTP dan `TC-AUTH-OTP-102`, yaitu `"You need to agree to the Privacy Policy to continue"`.

**Yang perlu diselaraskan:**  
Pemilik modul UX/UI perlu menyamakan copy pesan error checkbox di seluruh alur autentikasi (`login-password`, `login-otp`, dan `session-management`) agar konsisten menggunakan satu varian kalimat.

---

## GAP-OTP-E2E-004 — Divergensi Kebijakan Pencatatan Log pada Token Kedaluwarsa / Abandoned Layar Agreement

**Status:** terselesaikan via keputusan PRD Login OTP  
**Tipe:** divergensi arsitektur logging antar-fitur  
**Dampak:** tinggi untuk ketepatan assertion log  

Pada modul Login with Password (`login-password.md` §9.8 dan §11.4), jika layar Confirm to Continue ditinggalkan atau token pra-autentikasi kedaluwarsa secara natural, sistem mencatat entri `Failed` dengan Note `Consent not given` (GAP-LP-E2E-009).

Sebaliknya, pada modul Login with OTP:
- PRD `login-otp.md` §9.8 (Tabel Pencatatan baris Confirm Agreement tidak dikonfirmasi):
  > *"Confirm Agreement tidak dikonfirmasi (token expired atau layar ditinggalkan; tidak dicatat) ... Sync | Tidak dicatat"*
- Changelog `tc-login-otp.md` entri 2026-10-06 (GAP-393):
  > *"token kedaluwarsa atau layar ditinggalkan tidak dicatat (TC `TC-AUTH-OTP-109`, `TC-AUTH-OTP-111`). NC-12 digantikan keputusan ini."*
- `TC-AUTH-OTP-107` Expected Result (e):
  > *"Tidak ada baris baru untuk percobaan ini di kedua surface log"*

Artinya, pada Login with OTP, penolakan dan penulisan Note `Consent not given` **hanya terjadi jika tombol [Continue ➔] diklik secara aktif oleh pengguna tanpa mencentang checkbox** (`TC-AUTH-OTP-102` & `TC-AUTH-OTP-126`). Bila pengguna hanya mendiamkan layar hingga token 10 menit habis atau menutup tab, tidak ada entri log yang ditulis.

**Yang dilakukan di spec:**  
Spec `TC-AUTH-OTP-E2E-021` mengadopsi aturan terbaru PRD Login with OTP: memverifikasi bahwa penutupan layar atau kadaluwarsa token tidak menambah baris baru di kedua surface log, dan `Consent not given` hanya dicatat pada klik eksplisit tanpa centang.

---

## GAP-OTP-E2E-005 — Pembuktian Transaksi Database Atomik (EC-46) Membutuhkan Integration Test / Fault Injection

**Status:** terbuka, batas lapisan E2E UI  
**Tipe:** arsitektur backend non-UI observable  
**Dampak:** rendah untuk spec E2E, krusial untuk backend integration  

PRD `login-otp.md` §9.6 (Action Resilience) dan §9.4.2 EC-46 mensyaratkan bahwa konsumsi kode OTP dan pencatatan audit log harus berada dalam satu transaksi database atomik (jika penulisan log gagal, konsumsi kode di-rollback sehingga pengguna tidak kehilangan hak verifikasi).

Kondisi kegagalan parsial di mana penulisan log gagal secara internal di database tidak dapat disimulasikan dari blackbox UI browser tanpa injeksi kegagalan pada level koneksi database.

**Yang dilakukan di spec:**  
Aspek konkurensi dan integritas konsumsi atomik diuji di level browser melalui uji balapan tab paralel di `TC-AUTH-OTP-E2E-027` dan verifikasi simetris 1:1 di `TC-AUTH-OTP-E2E-011`. Uji kegagalan transaksi DB parsial diserahkan ke suite uji backend terpisah (`tc-login-otp-backend.md`).

---

## GAP-OTP-E2E-006 — Kebutuhan Test Harness Khusus Otomasi E2E

**Status:** terbuka, dicatat di Prerequisites tiap spec  
**Tipe:** kesiapan environment uji otomasi  
**Dampak:** memblokir eksekusi test runner jika harness belum tersedia  

Seluruh kebutuhan dependensi otomasi telah dicatat pada `## Prerequisites` masing-masing spec untuk panduan implementasi tim pengembang otomasi:

| Kebutuhan Harness | Deskripsi & Kegunaan | Spec yang Membutuhkan |
|---|---|---|
| **Mail-catcher API** | Menangkap kode OTP 6-digit dan mengukur SLA latensi pengiriman email (≤ 2 menit) | 001, 006, 010, 011, 012, 014, 015, 016, 020, 022 |
| **Server Clock Mock / Time-Travel** | Memanipulasi sisa waktu token (OTP 5 menit, preAuthToken 10 menit, Resend cooldown 10 menit) tanpa harus menunggu delay riil | 012, 015, 018, 021 |
| **TOTP Authenticator Generator** | Memasok kode faktor kedua time-based 6-digit untuk pengujian handoff MFA | 022 |
| **Data Seed State Akun** | Menyiapkan profil user: FIRST (login pertama), IDLE (>30 hari), POLICY (kebijakan privasi baru), NEWDEV (device baru), POLNEW, PENDING, INACTIVE, Suspended Client, Expired Client | 005, 011, 020, 021, 022, 024 |
| **Network Mock Interceptor** | Intercept endpoint HTTP untuk simulasi error 500, network drop/timeout, respons 429, dan payload tampering | 007, 008, 013, 026, 027 |
| **Multi-tab Context** | Pengujian tab paralel untuk mendeteksi race condition dan invalidasi lintas tab | 023, 027 |

---

## GAP-OTP-E2E-007 — Target Environment E2E Masih Mengarah ke Demo App

**Status:** terbuka  
**Tipe:** konfigurasi environment  
**Dampak:** memblokir eksekusi runner TestSpectra  

Konfigurasi `tagsamurai-e2e-test/spectra.config.ts` saat ini masih menggunakan URL target demo aplikasi bawaan framework TestSpectra. Untuk menjalankan suite `specs/Auth/LoginOtp/`, konfigurasi target `baseURL` harus diarahkan ke instance staging/testing web aplikasi TAG Samurai.

---

## Kepatuhan Suite Login OTP

- **Cakupan TC:** 100% (183 dari 183 TC granular aktif dari `TC-AUTH-OTP-01` sampai `TC-AUTH-OTP-183` terpetakan secara lengkap tanpa satu pun yang terlewat).
- **Duplikasi TC:** 0 (setiap `TC-AUTH-OTP-NN` hanya muncul tepat di satu spec).
- **Pembagian Platform:** 26 spec web, 1 spec mobile (`TC-AUTH-OTP-E2E-002`).
- **Verifikasi Lint:** `npx spectra lint --strict specs/Auth/LoginOtp` → `✓ 27 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`
- **Karakter Non-Kanonikal:** 0 karakter CJK atau full-width punctuation residue.
- **Status Spec:** Seluruh spec berstatus `draft` dengan struktur langkah uji bernomor lengkap, siap untuk fase pembuatan script otomasi (`tagsamurai-e2e-generate-script`).


---

# Gap & Temuan — Auth > MFA (Multi-Factor Authentication)

Sumber: generate spec `specs/Auth/Mfa/` (30 spec, 205 TC aktif). Tanggal generate: 2026-10-07.

Dokumen ini mencatat seluruh temuan, perbedaan langkah/prekondisi, dan celah cakupan yang diidentifikasi selama proses **audit silang antara PRD `auth/mfa/PRD/mfa.md` dan Test Case `auth/mfa/TestCases/tc-mfa.md`**.

---

## GAP-MFA-E2E-001 — Nilai threshold IP Rate Limit belum ditetapkan secara kuantitatif di PRD

**Status:** terbuka, bawaan PRD  
**Tipe:** `[TODO Engineering]`  
**Dampak:** tinggi untuk penentuan batas ekspektasi assert otomasi non-mock  

PRD `mfa.md` §9.2 dan `auth-foundation.md` §3.2 menandai batas IP rate limit sebagai `[TODO Engineering]`. Di sisi lain, `TC-AUTH-MFA-204` dan `TC-AUTH-MFA-205` menguji kondisi rate limit (status 429 dan caption "Too many requests. Please try again later.") dengan asumsi "threshold diturunkan di lingkungan uji". Angka eksak request per time-window (misal: 10 request per 60 detik per IP) belum didefinisikan secara resmi di dokumen PRD maupun TC.

**Yang dilakukan di spec:**  
Spec `TC-AUTH-MFA-E2E-030` mencakup skenario rate limit dengan `Mode: mock` (injeksi respons 429) dan memverifikasi perilaku UI:
1. Caption inline error "Too many requests. Please try again later." tampil di bawah kotak digit atau di form Choose Verification Method.
2. Nilai kotak digit dipertahankan (tidak dikosongkan).
3. Penolakan rate limit tidak menghasilkan entri baru di Activity Log Session maupun User Log.

**Yang perlu diputuskan tim Engineering:**  
Menetapkan angka batas request per window secara kuantitatif agar pengujian end-to-end terintegrasi tanpa mock dapat mengulang request dengan hitungan batas pasti.

---

## GAP-MFA-E2E-002 — Inkonsistensi Copy Header / Subtitle S-AUTHMFA-02 (OTP Verification)

**Status:** terselesaikan via konsensus NC-11  
**Tipe:** inkonsistensi copy antar seksi PRD  
**Dampak:** rendah hingga sedang, memengaruhi assertion teks UI  

Pada PRD wireframe `mfa.md` §4.2 Halaman 2 tertulis:  
> Subtitle: `"We sent a 6-digit code to user@company.com"`

Namun, pada `auth-foundation.md` §4.2, LLD MFA, dan keputusan konfirmasi NC-11 (2026-10-06):  
> Subtitle resmi yang disepakati adalah `"We sent a code to {email}"` (tanpa frase "6-digit" dan email tidak di-mask).

File `tc-mfa.md` (TC-04 dan TC-56) sudah menerapkan versi NC-11, namun wireframe PRD §4.2 belum diperbarui.

**Yang dipakai di spec:**  
Spec `TC-AUTH-MFA-E2E-002` mengadopsi copy resmi NC-11: `"We sent a code to {email}"`.

---

## GAP-MFA-E2E-003 — UI Feedback Penolakan Resend Sebelum Cooldown 60 Detik Berakhir

**Status:** terbuka  
**Tipe:** perbedaan UI guard vs Backend enforcement  
**Dampak:** rendah  

PRD `mfa.md` §9.2 F-AUTHMFA-04 menyatakan bahwa server menegakkan cooldown 1 menit: request resend yang masuk sebelum cooldown berakhir ditolak tanpa email dan tanpa menambah hitungan, serta UI tetap pada state cooldown tanpa toast atau caption baru.

Di `TC-AUTH-MFA-85`, pengujian ini menggunakan client HTTP / direct API call. Di level browser murni, tombol `[Resend code]` berada dalam kondisi `Disabled` dengan hitung mundur di dalam label tombol, sehingga interaksi klik pengguna secara fisik dicegah oleh UI.

**Yang dilakukan di spec:**  
`TC-AUTH-MFA-E2E-018` memverifikasi pencegahan di level UI (tombol disabled dengan countdown `Resend code in Ns`), sementara penolakan server jika request diterobos via API dicakup pada spec defense-in-depth `TC-AUTH-MFA-E2E-030`.

---

## GAP-MFA-E2E-004 — Penanganan Attestation Token pada Mobile App MFA

**Status:** terbuka  
**Tipe:** kelengkapan skenario mobile  
**Dampak:** sedang untuk tim pengembang mobile  

Pada modul Login with OTP (`login-otp.md` §4.6), mobile app menggunakan Google Play Integrity API untuk device attestation sebagai pengganti reCAPTCHA web. Pada PRD `mfa.md` §4.6, Mobile Layout hanya menyebut layout kartu, keypad numerik otomatis, dan penskalaan QR code enrollment. Belum ada spesifikasi apakah pengiriman OTP faktor-2 di mobile membutuhkan token Play Integrity baru atau murni bergantung pada validitas sesi pre-auth.

**Yang dilakukan di spec:**  
Spec `TC-AUTH-MFA-E2E-005` memverifikasi keypad numerik dan scaling layout mobile sesuai spesifikasi UI PRD §4.6. Rekomendasi disampaikan ke tim mobile untuk mengklarifikasi apakah Play Integrity token dibutuhkan saat pengiriman OTP faktor-2 di mobile.

---

## GAP-MFA-E2E-005 — Divergensi Penanganan Toast Sukses Antara Alur Login Biasa vs Enrollment Authenticator

**Status:** terselesaikan via PRD §7 (T-02)  
**Tipe:** perlakuan khusus notifikasi feedback  
**Dampak:** sedang  

PRD `mfa.md` §4.2 dan §7 (T-02) menetapkan bahwa setelah verifikasi enrollment berhasil, user langsung dialihkan ke Portal — Product Hub, dan toast sukses `"Success, authenticator app has been added."` tampil di pojok layar saat mendarat di Portal.

Sebaliknya, pada alur verifikasi faktor-2 biasa (OTP dan Authenticator yang sudah enroll), tidak ada toast sukses yang dimunculkan (sukses = redirect langsung ke Portal). Hal ini merupakan perlakuan khusus untuk mengonfirmasi aktivasi faktor baru kepada pengguna.

**Yang dilakukan di spec:**  
Spec `TC-AUTH-MFA-E2E-021` memverifikasi munculnya toast `"Success, authenticator app has been added."` saat mendarat di Portal pasca-enrollment, sedangkan spec verifikasi OTP (`016`) dan TOTP (`019`) memverifikasi redirect langsung tanpa toast sukses.

---

## GAP-MFA-E2E-006 — Kebutuhan Test Harness Khusus Otomasi E2E MFA

**Status:** terbuka, dicatat di Prerequisites tiap spec  
**Tipe:** kesiapan environment uji otomasi  
**Dampak:** memblokir eksekusi test runner jika harness belum tersedia  

Seluruh kebutuhan dependensi otomasi telah dicatat pada `## Prerequisites` masing-masing spec untuk panduan implementasi tim pengembang otomasi:

| Kebutuhan Harness | Deskripsi & Kegunaan | Spec yang Membutuhkan |
|---|---|---|
| **Mail-catcher API** | Menangkap email kode OTP faktor-2, mengukur SLA pengiriman, dan membaca email alert unusual login | 008, 010, 011, 012, 014, 016, 018, 023, 027, 028, 030, 033, 034, 035 |
| **TOTP Authenticator Helper (RFC 6238)** | Memasok kode faktor kedua time-based 6-digit (SHA-1, periode 30 detik) serta simulasi drift window ±1 step | 003, 019, 020, 021, 022, 023, 024, 028, 030, 032, 033 |
| **Server Clock Mock / Time-Travel** | Memanipulasi sisa waktu token (TTL pre-auth 10 menit, OTP expired >5 menit, tumbling window 90 hari, dan decay pasangan negara 180 hari) | 012, 013, 017, 018, 024 |
| **Geo-IP Location & IP Injector** | Mensimulasikan login dari IP Jakarta, Surabaya (>100 km), Batam, dan Singapura (beda negara) serta kegagalan geo-IP (fail-open) | 007, 010, 011, 012, 013, 014, 027 |
| **QR Code Image / Canvas Decoder (`jsQR`)** | Ekstraksi dan decoding gambar/canvas QR Code untuk memeriksa parameter RFC 6238 `otpauth://totp/` | 032 |
| **Data Seed State Akun** | Menyiapkan profil user: FIRST, NEWDEV, NEWDEVE, IDLE, FAR, XC, XCT, MOB, AGR, PLAT2, Suspended/Expired Client, Distributor, Partner, Principal | 001, 007, 008, 009, 010, 011, 012, 013, 014, 015, 023, 025, 026, 030, 031, 036 |
| **Network Mock Interceptor** | Intercept endpoint HTTP untuk simulasi error 500, timeout, respons 429, dan payload tampering | 014, 018, 027, 034, 035 |
| **Multi-tab Context & Multi-device** | Pengujian tab paralel untuk mendeteksi race condition, verifikasi bersamaan, dan pembatalan sesi lintas tab/device | 025, 031, 033 |

---

## GAP-MFA-E2E-007 — Target Environment E2E Masih Mengarah ke Demo App

**Status:** terbuka  
**Tipe:** konfigurasi environment  
**Dampak:** memblokir eksekusi runner TestSpectra  

Konfigurasi `tagsamurai-e2e-test/spectra.config.ts` saat ini masih menggunakan URL target demo aplikasi bawaan framework TestSpectra. Untuk menjalankan suite `specs/Auth/Mfa/`, konfigurasi target `baseURL` harus diarahkan ke instance staging/testing web aplikasi TAG Samurai.

---

## GAP-MFA-E2E-008 — Pemisahan Uji Kompleksitas Tinggi dari Spec Screening dan Dekomposisi Modular (30 → 36 Specs)

**Status:** terselesaikan via restrukturisasi arsitektur spec E2E (2026-10-07)  
**Tipe:** arsitektur test case & isolasi eksekusi otomasi  
**Dampak:** tinggi terhadap stabilitas otomasi Playwright dan kecepatan diagnosis kegagalan  

Pada draf awal generasi spec E2E (30 spec), ditemukan pola *cramming* atau penggabungan beberapa pengujian teknis tingkat tinggi ke dalam satu spec screening visual atau spec fungsional biasa:
1. **Decoding QR Code Canvas di Spec Screening (`TC-AUTH-MFA-109` di Spec 004):** Pengujian inspeksi visual Step 1-3 form enrollment digabung dengan decoding gambar/canvas QR code untuk memvalidasi URI `otpauth://totp/` dan parameter RFC 6238 (SHA1, 30s period, secret string). Ini memaksa spec screening visual bergantung pada library decoder eksternal (`jsQR`).
2. **Polling Mail-Catcher di Spec Screening OTP (`TC-AUTH-MFA-62` di Spec 002):** Spec screening tata letak kotak SegmentedInput dan navigasi Backspace digabung dengan request polling kotak masuk email mail-catcher, memperlambat eksekusi screening visual.
3. **Mock Hardware Biometrik di Spec Layout Mobile (`TC-AUTH-MFA-54` di Spec 005):** Pengujian tata letak keypad numerik responsif Android dicampur dengan instrumentasi sensor biometrik (fingerprint / face unlock) pada faktor-1.
4. **Verifikasi Admin GS di Skenario User Biasa (`TC-AUTH-MFA-178` di Spec 026):** Skenario penundaan pencatatan log Success ke faktor-2 menuntut login sebagai Total Control Global Settings di tengah-tengah alur device fingerprinting user browser biasa.
5. **Mega-Specs Heterogen (Spec 028, 029, 030):** Menggabungkan race condition multi-tab/device, flood IP rate limit 429, fault injection 5xx, screen reader ARIA Live, direct API tampering, fallback lost-device, dan paritas tier langganan ke dalam spec yang terlalu padat (16–18 TC per file).

**Dampak Buruk Jika Tidak Dipecah:**
- **Flakiness tinggi:** Kegagalan library decoding QR atau polling email akan menggagalkan seluruh assertion layout screening tombol/input, menyamarkan apakah bug ada pada CSS/DOM atau pada backend format.
- **Fixture berlebih:** Mengharuskan setiap runner menyiapkan konteks multi-tab, proxy hop, dan mail-catcher bahkan untuk pengetesan form sederhana.
- **Diagnosis sulit:** CI/CD reporting gagal menunjukkan akar penyebab secara presisi.

**Solusi & Keputusan yang Diterapkan di Spec:**  
Dilakukan dekomposisi modular menjadi **36 spec terisolasi**:
- `TC-109` (QR URI decode) dipindahkan ke spec khusus **`TC-AUTH-MFA-E2E-032`** (*Verifikasi Kriptografis Isi QR Code & Secret Key*).
- `TC-62` (cek mail-catcher) dipindahkan dari Spec 002 ke **`TC-AUTH-MFA-E2E-016`** (*Verifikasi OTP Auto-Submit & Paste*).
- `TC-54` (biometric hardware) dipisahkan menjadi spec khusus **`TC-AUTH-MFA-E2E-036`** (*Mobile Biometric Re-Login Trigger*).
- `TC-178` (delayed success logging) dipindahkan dari Spec 026 ke **`TC-AUTH-MFA-E2E-028`** (*Audit Log Status Mutasi*).
- Uji balapan multi-tab/device dikonsolidasikan ke **`TC-AUTH-MFA-E2E-033`** (*Konkurensi & Double-Submit Guards*).
- Uji API token tampering dikonsolidasikan ke **`TC-AUTH-MFA-E2E-034`** (*Defense-in-Depth Token Tampering*).
- Uji flood 429 dan 5xx server fault injection diisolasi di **`TC-AUTH-MFA-E2E-035`** (*Rate Limiting & Resilience*).
- Uji recovery user dan admin reset dipisahkan di **`TC-AUTH-MFA-E2E-030`**, sementara paritas subscription & dialog session management diisolasi di **`TC-AUTH-MFA-E2E-031`**.

---

## Kepatuhan Suite MFA

- **Cakupan TC:** 100% (205 dari 205 TC granular aktif dari `TC-AUTH-MFA-01` sampai `TC-AUTH-MFA-205` terpetakan secara lengkap tanpa satu pun yang terlewat).
- **Duplikasi TC:** 0 (setiap `TC-AUTH-MFA-NN` hanya muncul tepat di satu spec).
- **Pembagian Platform:** 34 spec web, 2 spec mobile (`TC-AUTH-MFA-E2E-005` layout responsif & `TC-AUTH-MFA-E2E-036` biometric re-login).
- **Verifikasi Lint:** `npx spectra lint --strict specs/Auth/Mfa` → `✓ 36 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`
- **Karakter Non-Kanonikal:** 0 karakter CJK atau full-width punctuation residue.
- **Status Spec:** Seluruh 36 spec berstatus `draft` dengan isolasi tanggung jawab tinggi (UI screening, cryptography, race condition, rate limiting, dan audit log terpisah), siap untuk fase pembuatan script otomasi (`tagsamurai-e2e-generate-script`).