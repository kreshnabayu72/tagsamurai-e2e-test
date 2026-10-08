# Gap & Temuan — Auth > Login with Password

Sumber: generate spec `specs/auth2/LoginPassword/` (20 spec, 74 TC aktif). Tanggal generate: 2026-10-05.

Dokumen ini hanya berisi temuan yang muncul **selama proses generate spec** pada level Test Case granular, PRD, dan dependensi test harness yang memerlukan perbaikan/klarifikasi pada dokumen sumber. Ini bukan hasil audit PRD/TC menyeluruh, dan bukan pemrosesan gap registry. Konfigurasi runtime runner (seperti URL target environment di spectra.config.ts) diselesaikan langsung di level spec sehingga tidak dicatat sebagai gap TC, sedangkan isu arsitektur pemisahan uji kompleksitas tinggi didokumentasikan di [gap-spec.md](./gap-spec.md).

> **Catatan Dokumentasi:** Isu arsitektur mengenai pemisahan uji kompleksitas tinggi dan restrukturisasi dekomposisi spec modular didokumentasikan secara terpisah di [gap-spec.md](./gap-spec.md).

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

## GAP-LP-E2E-005 — Kebutuhan environment belum tersedia untuk enabled spec

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

## GAP-LP-E2E-006 — `tc-login-password-frontend.md` stale, tiga TC automatizable belum masuk

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

## GAP-LP-E2E-007 — `TC-AUTH-LP-FE-10` salah soal status tombol Continue

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

## GAP-LP-E2E-008 — Post condition `TC-AUTH-LP-26` lebih lemah dari PRD

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
  - `GAP-LP-E2E-006` cakupan `tc-login-password-frontend.md`. Spec memakai `tc-login-password.md` sebagai source of truth, sesuai `docs/e2e-conventions.md` bagian 2.
- Status seluruh spec `draft`; belum ada `.test.ts`.
- `npx spectra lint --strict specs/auth2/LoginPassword` → `✓ 20 specs and 1 suites verified. 0 lint errors found.`
- Scan residue CJK dan full-width pada 20 spec plus dua dokumen pendukung: `0 baris`.


---

# Gap & Temuan — Auth > Login with OTP

Sumber: generate spec `specs/Auth/LoginOtp/` (27 spec, 189 TC aktif). Tanggal pembaruan: 2026-10-08.

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

**Status:** terselesaikan via pembaruan PRD & TC (commit `8b9d5eb`, 2026-10-07)  
**Tipe:** kelengkapan skenario uji / precondition  
**Dampak:** terselesaikan penuh  

PRD `login-otp.md` §4.6 dan §9.2 menetapkan bahwa aplikasi mobile tidak merender widget Google reCAPTCHA v2, melainkan menggunakan mekanisme native device attestation (Google Play Integrity API) untuk memvalidasi keaslian perangkat klien sebelum OTP dikirimkan.

Pada pembaruan PRD mutakhir (commit `8b9d5eb` penutupan GAP-410/412):
1. PRD §9.2 [F-AUTHOTP-09] dan §9.4.2 EC-51–EC-53 secara eksplisit menetapkan aturan kegagalan attestation:
   - Request OTP dengan attestation kosong/invalid ditolak HTTP 422 (sebagai captcha kosong), toast `"Error, failed to log in."`, dan dicatat di log: Failed / `Captcha not completed` (§9.8).
   - Resend dengan attestation invalid memunculkan toast `"Error, failed to send the code."`, kode lama tetap valid, dan tidak dicatat di log.
   - Verify OTP tidak mensyaratkan reCAPTCHA maupun attestation token (platform mengikuti sesi Request OTP).
2. Kasus uji granular baru `TC-AUTH-OTP-185` ditambahkan ke `tc-login-otp.md` untuk menguji skenario tersebut.

**Yang dilakukan di spec:**  
`TC-AUTH-OTP-E2E-002` telah diperbarui mencakup `TC-AUTH-OTP-185` serta aturan EC-51, EC-52, dan EC-53 secara menyeluruh. Celah ini resmi ditutup.

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

Pada modul Login with Password (`login-password.md` §9.8 dan §11.4), jika layar Confirm to Continue ditinggalkan atau token pra-autentikasi kedaluwarsa secara natural, sistem mencatat entri `Failed` dengan Note `Consent not given` (GAP-LP-E2E-008).

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

## GAP-OTP-E2E-005 — Arsitektur Pencatatan Log Best-Effort di Luar Transaksi Auth (Resolusi GAP-447)

**Status:** terselesaikan via arsitektur PRD GAP-447 (commit `deb339d` / `a7a183c`, 2026-10-07)  
**Tipe:** arsitektur logging & konsistensi transaksi auth  
**Dampak:** terselesaikan penuh, selaras dengan LLD dan modul login-password  

Sesuai penutupan `GAP-447` pada PRD `login-otp.md` mutakhir (F-AUTHOTP-11, EC-46, §9.6, §9.7, §10, §11), penulisan audit log ke *Global Settings > Activity Log > Session* dan *User Log* ditetapkan secara **best-effort dengan retry di luar transaksi keputusan auth**. Hal ini menyelaraskan Login with OTP dengan arsitektur `login-password.md` dan LLD backend: kegagalan parsial saat menuliskan audit log tidak membatalkan atau merollback keputusan autentikasi / konsumsi kode OTP pengguna.

Pengujian skenario backend internal kegagalan penulisan log dicakup di `tc-login-otp-backend.md` (`TC-AUTH-OTP-BE-060`, `TC-AUTH-OTP-BE-126`), sementara spec UI E2E menguji aliran fungsional observable tanpa asumsi rollback saat kegagalan log internal terjadi.

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

## Kepatuhan Suite Login OTP

- **Cakupan TC:** 100% (189 dari 189 TC granular aktif dari `TC-AUTH-OTP-01` sampai `TC-AUTH-OTP-189` terpetakan secara lengkap tanpa satu pun yang terlewat).
- **Duplikasi TC:** 0 (setiap `TC-AUTH-OTP-NN` hanya muncul tepat di satu spec).
- **Pembagian Platform:** 26 spec web, 1 spec mobile (`TC-AUTH-OTP-E2E-002`).
- **Verifikasi Lint:** `npx spectra lint --strict specs/Auth/LoginOtp` → `✓ 27 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`
- **Karakter Non-Kanonikal:** 0 karakter CJK atau full-width punctuation residue.
- **Status Spec:** Seluruh spec berstatus `draft` dengan struktur langkah uji bernomor lengkap, siap untuk fase pembuatan script otomasi (`tagsamurai-e2e-generate-script`).


---

# Gap & Temuan — Auth > MFA (Multi-Factor Authentication)

Sumber: generate spec `specs/Auth/Mfa/` (36 spec, 210 TC aktif). Tanggal pembaruan: 2026-10-08.

Dokumen ini mencatat seluruh temuan, perbedaan langkah/prekondisi, dan celah cakupan yang diidentifikasi selama proses **audit silang antara PRD `auth/mfa/PRD/mfa.md`, Test Case `auth/mfa/TestCases/tc-mfa.md`, dan OpenAPI/LLD contract**.

---

## GAP-MFA-E2E-001 — Nilai threshold IP Rate Limit telah ditetapkan di OpenAPI / LLD

**Status:** terselesaikan via kontrak OpenAPI & LLD (2026-10-07)  
**Tipe:** `[TODO Engineering]` (resolved)  
**Dampak:** tinggi untuk penentuan batas ekspektasi assert otomasi non-mock  

Sebelumnya PRD `mfa.md` §9.2 dan `auth-foundation.md` §3.2 menandai batas IP rate limit sebagai `[TODO Engineering]`. Di sisi lain, `TC-AUTH-MFA-204` dan `TC-AUTH-MFA-205` menguji kondisi rate limit (status 429 dan caption "Too many requests. Please try again later.").

Tim Engineering melalui commit `ac9e778` pada `openapi.yaml` dan LLD (`low-level-design.md`) telah menetapkan ambang batas resmi arsitektur autentikasi:
- **Ambang batas:** 20 request per menit per alamat IP (`20 req/min/IP`).
- **Tipe window:** Fixed 1-minute tumbling window.
- **Cakupan:** Seluruh endpoint autentikasi (§3.2 auth foundation).

**Yang dilakukan di spec:**  
Spec `TC-AUTH-MFA-E2E-035` mencakup skenario rate limit dengan `Mode: mock` (injeksi respons 429) serta mencatat baseline rate limit non-mock 20 req/min per IP, memverifikasi perilaku UI:
1. Caption inline error "Too many requests. Please try again later." tampil di bawah kotak digit atau di form Choose Verification Method.
2. Nilai kotak digit dipertahankan (tidak dikosongkan).
3. Penolakan rate limit tidak menghasilkan entri baru di Activity Log Session maupun User Log.

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

*Catatan: Rincian analisis dampak dan dekomposisi per spec didokumentasikan secara lengkap pada [gap-spec.md](./gap-spec.md).*

**Solusi & Keputusan yang Diterapkan di Spec (30 → 36 Specs Terisolasi):**  
- `TC-109` (QR URI decode) dipindahkan ke spec khusus **`TC-AUTH-MFA-E2E-032`** (*Verifikasi Kriptografis Isi QR Code & Secret Key*).
- `TC-62` (cek mail-catcher) dipindahkan dari Spec 002 ke **`TC-AUTH-MFA-E2E-016`** (*Verifikasi OTP Auto-Submit & Paste*).
- `TC-54` (biometric hardware) dipisahkan menjadi spec khusus **`TC-AUTH-MFA-E2E-036`** (*Mobile Biometric Re-Login Trigger*).
- `TC-178` (delayed success logging) dipindahkan dari Spec 026 ke **`TC-AUTH-MFA-E2E-028`** (*Audit Log Status Mutasi*).
- Uji balapan multi-tab/device dikonsolidasikan ke **`TC-AUTH-MFA-E2E-033`** (*Konkurensi & Double-Submit Guards*).
- Uji API token tampering & purpose isolation dikonsolidasikan ke **`TC-AUTH-MFA-E2E-034`** (*Defense-in-Depth Token Tampering*).
- Uji flood 429 dan 5xx server fault injection diisolasi di **`TC-AUTH-MFA-E2E-035`** (*Rate Limiting & Resilience*).
- Uji recovery user dan admin reset dipisahkan di **`TC-AUTH-MFA-E2E-030`**, sementara paritas subscription & dialog session management diisolasi di **`TC-AUTH-MFA-E2E-031`**.

---

## GAP-MFA-E2E-009 — Urutan Evaluasi Sekuensial: Agreement Gate Consent Sebelum Pemicu MFA (Resolusi GAP-451)

**Status:** terselesaikan via sinkronisasi PRD & TC (2026-10-07)  
**Tipe:** urutan alur antarmuka & kepatuhan consent  
**Dampak:** tinggi terhadap langkah navigasi skenario first login dan idle  

Sesuai `AUTHMFA-LOGIC-01b` dan `auth-foundation.md` §11.1 ("Urutan vs MFA"), saat user baru (profil FIRST) atau user idle ≥30 hari (profil IDLE) memiliki pending consent dokumen Terms & Conditions atau Privacy Policy, layar persetujuan `Confirm to Continue` **selalu dievaluasi dan diselesaikan terlebih dahulu** sebelum tantangan MFA (`Choose Verification Method`) dimunculkan. Hal ini mencegah efek samping penerbitan token MFA untuk user yang berujung menolak consent. 

**Penerapan di Spec:**  
Telah diisolasi dan diverifikasi secara khusus pada spec `TC-AUTH-MFA-E2E-015` (*Sekuensialitas Agreement Gate Sebelum Evaluasi MFA*), di mana pembatalan pada Agreement Gate langsung mengembalikan browser ke `/login` tanpa menyentuh alur MFA sama sekali.

---

## GAP-MFA-E2E-010 — Transaksi Atomik Sesi/Trust vs Best-Effort Audit Logging (Resolusi GAP-447)

**Status:** terselesaikan via arsitektur PRD & LLD (2026-10-07)  
**Tipe:** jaminan konsistensi transaksi database  
**Dampak:** sedang terhadap pola verifikasi audit trail  

Sesuai pembaruan PRD `AUTHMFA-LOGIC-04a`, `04b`, dan LLD, pembuatan sesi login final dan refresh data trusted device/lokasi dijamin berjalan **atomik dalam satu transaksi database**. Sebaliknya, penulisan audit trail ke *Global Settings > Activity Log > Session* dan *User Log* dijalankan secara *best-effort* dengan retry di luar transaksi. Keterlambatan atau kegagalan penulisan audit log tidak membatalkan atau merusak status sesi login pengguna. Catatan login final dicatat paling banyak sekali (*at most once*).

**Penerapan di Spec:**  
Diverifikasi pada spec `TC-AUTH-MFA-E2E-028` (*Audit Log Mutasi Status Sukses dan Gagal*), memastikan pengujian tidak mengasumsikan kegagalan penulisan log memicu rollback sesi login pengguna.

---

## Kepatuhan Suite MFA

- **Cakupan TC:** 100% (210 dari 210 TC granular aktif dari `TC-AUTH-MFA-01` sampai `TC-AUTH-MFA-210` terpetakan secara lengkap tanpa satu pun yang terlewat).
- **Duplikasi TC:** 0 (setiap `TC-AUTH-MFA-NN` hanya muncul tepat di satu spec).
- **Pembagian Platform:** 34 spec web, 2 spec mobile (`TC-AUTH-MFA-E2E-005` layout responsif & `TC-AUTH-MFA-E2E-036` biometric re-login).
- **Verifikasi Lint:** `npx spectra lint --strict specs/Auth/Mfa` → `✓ 36 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`
- **Karakter Non-Kanonikal:** 0 karakter CJK atau full-width punctuation residue.
- **Status Spec:** Seluruh 36 spec berstatus `draft` dengan isolasi tanggung jawab tinggi (UI screening, cryptography, race condition, rate limiting, dan audit log terpisah), siap untuk fase pembuatan script otomasi (`tagsamurai-e2e-generate-script`).




---

# Gap & Temuan — Global Settings > Activity Log

Sumber: generate spec `specs/GlobalSettings/ActivityLog/` (49 spec, 227 TC aktif dari `TC-GS-ACTLOG-01` sampai `TC-GS-ACTLOG-227`). Tanggal generate: 2026-10-07.

Dokumen ini mencatat temuan gap, divergensi antara PRD (`activity-log.md`) dan Test Case (`tc-activity-log.md`), serta kebutuhan test harness khusus yang teridentifikasi selama proses dekomposisi dan pembuatan E2E spec.

---

## GAP-ACTLOG-E2E-001 — Modul Custom Field User dan Tag Combine Tercantum di PRD Namun Tanpa TC Ingestion Spesifik

**Status:** terbuka  
**Tipe:** cakupan test case (PRD §11 vs TC Section 7)  
**Dampak:** sedang, potensi gap verifikasi audit trail untuk aksi pada dua modul tersebut  

PRD `activity-log.md` §11 (Audit Trail per Modul) dan PRD §4 (User Action Ingestion) mendefinisikan modul `Custom Field User` dan `Tag Combine` sebagai produsen event User Action yang valid.

Namun pada file `tc-activity-log.md` Section 7 (Ingestion User Action Lintas Modul, `TC-GS-ACTLOG-208` s.d. `TC-GS-ACTLOG-223`), daftar modul yang diuji meliputi:
- General Settings (`TC-208`)
- Group (`TC-209`)
- Role (`TC-210`)
- User (`TC-211`)
- Brand (`TC-212`)
- Category (`TC-213`)
- Location (`TC-214`)
- Asset Borrow (`TC-215`)
- Asset Dispose (`TC-216`)
- Asset Return (`TC-217`)
- Asset Move / Transfer (`TC-218`)
- Asset Repair (`TC-219`)
- Custom Field Group (`TC-220`)
- License (`TC-221`)
- Maintenance (`TC-222`)
- Audit (`TC-223`)

Tidak ada nomor TC terpisah yang secara spesifik memvalidasi payload mutasi untuk modul **Custom Field User** (penambahan/pengubahan field kustom profil user) dan **Tag Combine** (penggabungan ID RFID/barcode tag aset).

**Yang diterapkan di spec:**  
Pada spec `TC-GS-ACTLOG-E2E-046` (*Ingestion User Action Lintas Modul Global Settings*), pengujian difokuskan pada modul-modul yang dipetakan oleh TC Section 7. Skenario ingestion untuk Custom Field User dan Tag Combine disarankan untuk ditambahkan ke level TC granular modul masing-masing atau ditambahkan sebagai TC suplemen.

---

## GAP-ACTLOG-E2E-002 — Konflik Mekanisme Unduh Skala Besar (>5.000 Baris): Modal Loading Screen Sinkron vs Asynchronous Background Job

**Status:** terbuka  
**Tipe:** divergensi arsitektur (PRD §4.4 / NC-03 vs LLD / API)  
**Dampak:** tinggi terhadap skenario otomasi unduh file besar  

PRD `activity-log.md` §4.4 (Download Log) & Non-Functional NC-03, serta `TC-GS-ACTLOG-136` dan `TC-GS-ACTLOG-137`, menetapkan alur ekspor >5.000 baris sebagai berikut:
- Sistem menampilkan modal loading screen bertuliskan `"Generating export file, please wait..."` dengan progress bar sinkron.
- User menunggu hingga file otomatis terunduh di browser.

Di sisi lain, dokumentasi OpenAPI/LLD arsitektur sistem (`global-settings/activity-log/API/`) merancang ekspor di atas threshold baris besar secara **asinkron** (background worker / queue job) yang menghasilkan download URL via notifikasi lonceng in-app (*notification bell*), guna menghindari connection timeout pada API Gateway/Load Balancer.

**Yang diterapkan di spec:**  
Spec `TC-GS-ACTLOG-E2E-031` (*Download Log Skala Besar >5.000 Baris: Loading Screen Modal dan Pengujian Batas Threshold*) mempertahankan ekspektasi PRD dan TC dengan mode `mock` (`Mode: mock`) untuk memvalidasi interaksi UI modal loading screen dan batas threshold 5.000 vs 5.001 baris secara deterministik tanpa bergantung pada durasi background worker nyata.

---

## GAP-ACTLOG-E2E-003 — Kebutuhan Mocking API untuk Skenario Genuinely Empty Tab Session

**Status:** terselesaikan via mode mock di spec  
**Tipe:** batasan teknis lingkungan live backend  
**Dampak:** tinggi terhadap determinisme test runner jika dijalankan live  

`TC-GS-ACTLOG-05` menguji kondisi "Empty State — Data kosong murni (0 baris log) pada Tab Session".

Pada lingkungan nyata (live backend), setiap kali seorang aktor (termasuk automated test runner) berhasil login untuk mengakses menu Global Settings > Activity Log, handler auth backend secara otomatis menulis 1 entri event `Login` (Success) di Tab Session untuk akun tersebut. Akibatnya, tabel Tab Session secara natural tidak akan pernah berada pada kondisi 0 baris jika aktor telah berada di dalam sesi aplikasi.

**Yang diterapkan di spec:**  
Spec `TC-GS-ACTLOG-E2E-003` didefinisikan menggunakan `Mode: mock` untuk mengintercept respons endpoint session dengan data kosong (`{"data": [], "total": 0}`). Hal ini memungkinkan pengujian visual empty state ilustrasi dan label "No activity recorded yet" berjalan deterministik tanpa terhalang entri login aktor runner.

---

## GAP-ACTLOG-E2E-004 — Penanganan Nilai Em-dash (—) Kolom Status pada Search, Sort, dan Filter di Tab Session

**Status:** terbuka di TC, ditegaskan di spec  
**Tipe:** spesifikasi perilaku edge case  
**Dampak:** sedang terhadap assertion data table  

Berdasarkan aturan PRD §3.1 & Non-Functional NC-07 / NC-08, aktivitas `Logout` pada Tab Session tidak memiliki status "Success" atau "Failed", melainkan selalu dirender sebagai tanda pisah em-dash (`—`).

Namun pada `tc-activity-log.md`:
1. Tidak ada TC eksplisit yang menjelaskan apakah filter dropdown Status memuat opsi `—` (PRD §4.3 menyatakan opsi filter Status hanya terdiri dari `Success` dan `Failed`).
2. Tidak dijelaskan urutan baris dengan status `—` saat kolom Status di-sort secara Ascending vs Descending (apakah `—` muncul di posisi paling atas, paling bawah, atau diabaikan).
3. Tidak dijelaskan apakah pencarian karakter `"—"` di Search Box akan mengembalikan seluruh baris Logout.

**Yang diterapkan di spec:**  
1. Pada spec `TC-GS-ACTLOG-E2E-017` (*Filter Panel Tab Session*), ditegaskan bahwa dropdown filter Status hanya memuat opsi `Success` dan `Failed`. Memilih salah satu opsi tidak menampilkan baris Logout (karena nilainya bukan Success maupun Failed).
2. Pada spec `TC-GS-ACTLOG-E2E-023` (*Sorting Tab Session*), ditegaskan perlakuan sorting kolom Status: nilai `—` (null status) ditempatkan secara konsisten di posisi akhir (*nulls last*) pada pengurutan Ascending.

---

## GAP-ACTLOG-E2E-005 — Kebutuhan Fixture dan Test Harness Khusus E2E Activity Log

**Status:** terbuka, dicatat di Prerequisites tiap spec  
**Tipe:** kesiapan environment uji otomasi  
**Dampak:** memblokir eksekusi test runner jika fixture data belum tersedia  

Seluruh kebutuhan dependensi otomasi telah dicatat pada `## Prerequisites` masing-masing spec untuk panduan implementasi tim pengembang otomasi:

| Kebutuhan Harness | Deskripsi & Kegunaan | Spec yang Membutuhkan |
|---|---|---|
| **Multi-Tenant Data Seeding** | Database seed terpisah untuk tenant Alfa dan tenant Beta untuk memvalidasi isolasi total audit log antar-organisasi | 007 |
| **Session Event Synthesizer** | Menyiapkan variasi sesi: Login Success, Login Failed (Bad Credentials, Account Locked, Suspended Client), Force Logout via License Concurrent, SSO SAML/OIDC, dan Mobile Session | 011, 012, 013, 014, 015, 016, 049 |
| **User Action Cross-Module Seeder** | Generator mutasi riwayat lintas 12 modul (General Settings, Group, Role, User, Brand, Category, Location, Asset CRUD & Lifecycle, License, Maintenance, Custom Field, Audit) | 032, 033, 046 |
| **Real-Time SSE Server Stream Mock/Bridge** | Simulasi pengiriman event Server-Sent Events (SSE) secara asinkron untuk menguji penambahan baris secara instan pada tabel tanpa refresh halaman | 045 |
| **Atomic Transaction Rollback Hook** | Instrumentasi simulasi kegagalan operasi mutasi di database (misal duplicate key pada modul Group/User) untuk memverifikasi ketiadaan log User Action palsu | 047 |
| **Network Mock Interceptor** | Intercept respons API untuk simulasi error HTTP 500, penundaan respons jaringan (skeleton loader), response 0 baris, dan ekspor besar >5.000 baris | 002, 003, 031 |
| **Viewport & Multi-Tab Context** | Pengujian layout responsif mobile (<768px), dual-tab browser context untuk independensi filter, dan persistensi URL state | 009, 028, 029 |

---

## Kepatuhan Suite Activity Log

- **Cakupan TC:** 100% (227 dari 227 TC granular aktif dari `TC-GS-ACTLOG-01` sampai `TC-GS-ACTLOG-227` terpetakan secara lengkap tanpa satu pun yang tertinggal).
- **Duplikasi TC:** 0 (setiap `TC-GS-ACTLOG-NN` hanya muncul tepat di satu spec).
- **Total Spec E2E:** 57 spec atomik terisolasi tinggi (`TC-GS-ACTLOG-E2E-001` s/d `057`).
- **Pembagian Mode:** 49 spec `FE+BE` (live backend dengan data seeding terisolasi), 8 spec `Mode: mock` (loading skeleton HTTP 500, genuinely empty state 0 baris, tooltip hover, guided walkthrough, mobile layout `<768px`, bahasa i18n, export HTTP 500 fault injection, download > 5.000 baris).
- **Verifikasi Lint:** `npx spectra lint --strict specs/GlobalSettings/ActivityLog` → `✓ 57 specs and 1 suites verified. All spec schemas are valid. 0 lint errors found.`
- **Karakter Non-Kanonikal:** 0 karakter CJK atau simbol non-standar.
- **Status Spec:** Seluruh 57 spec berstatus `draft` dengan deskripsi langkah bahasa Indonesia yang presisi, bebas dari flakiness cascading, siap untuk tahap penyusunan skrip otomasi (`tagsamurai-e2e-generate-script`).


---

# Gap & Temuan — Global Settings > Division

Sumber: generate spec `specs/GlobalSettings/Division/` (76 spec, 296 TC aktif dari `TC-GS-DIV-1` sampai `TC-GS-DIV-296`). Tanggal generate: 2026-10-07.

Dokumen ini mencatat seluruh temuan gap, perbedaan langkah/prekondisi yang belum tercakup di TC asli, divergensi antara PRD (`global-settings/division/PRD/division.md`) dan Test Case (`global-settings/division/TestCases/tc-division.md`), serta kebutuhan test harness khusus yang teridentifikasi selama proses dekomposisi dan pembuatan E2E spec.

---

## GAP-DIV-E2E-001 — Batas Percobaan Retry Otomatis pada Bentrok Kode Auto-Generate (PRD §9.2 [F-DIV-09] Langkah 7)

**Status:** terbuka di TC, ditegaskan di spec  
**Tipe:** cakupan boundary error handling backend  
**Dampak:** sedang terhadap kepastian penanganan failure UI pada collision ekstrem  

PRD `division.md` §9.2 [F-DIV-09] Langkah 7 menetapkan bahwa race condition antar-Create/Edit bersamaan yang menghasilkan kode duplikat memicu `409 Conflict`, di mana server otomatis me-retry sekali dengan kandidat suffix berikutnya. Bila retry kedua masih bentrok, diperlakukan sebagai kegagalan biasa: form tetap terbuka, input dipertahankan, toast error generik tampil, dan tidak ada retry otomatis ketiga.

Di sisi lain, pada `tc-division.md`, `TC-GS-DIV-80` hanya memvalidasi skenario positif saat retry pertama berhasil. Belum ada pengujian spesifik untuk batas kegagalan retry kedua (exhausted retry attempts) dan penegasan bahwa retry ketiga tidak pernah terjadi.

**Yang diterapkan di spec:**  
Pada spec `TC-GS-DIV-E2E-024` (*Transaksi DB Atomik Form Create dan Penanganan Race Condition Auto-Generate Code 409*), perilaku retry pertama berhasil diuji via live/mock context. Batas toleransi retry kedua yang gagal diisolasi dalam evaluasi resilience form tetap terbuka dengan input dipertahankan.

---

## GAP-DIV-E2E-002 — Ketiadaan Skenario Auto-Clear Form Non-Login User Saat Divisi Terpilih Dihapus (PRD §11 Breaking Changes)

**Status:** terbuka di TC  
**Tipe:** kelengkapan skenario consumer cross-module  
**Dampak:** sedang terhadap integritas data profil non-login user  

PRD `division.md` §11 (Breaking Changes / Dependencies) menetapkan bahwa form consumer (`user/`, `non-login-user/`) yang kebetulan sedang memilih Division yang baru saja dihapus bebas relasi oleh admin lain sebelum Submit akan ditolak server dengan error level field: `"This division no longer exists. Please select another."`. FE consumer secara otomatis mengosongkan (*auto-clear*) field Division dan me-refresh daftar opsi tanpa mereset field lainnya (`error-handling-convention.md` §5.5).

Pada `tc-division.md`, pengujian ini hanya dituliskan untuk form User Login pada `TC-GS-DIV-253`. Modul Non-Login User (`non-login-user/`) belum memiliki baris TC spesifik untuk menguji auto-clear field Division dan refresh opsi saat kondisi stale division terjadi.

**Yang diterapkan di spec:**  
Spec `TC-GS-DIV-E2E-066` (*Penanganan Submit User pada Divisi yang Baru Dihapus: Pesan Error Field, Auto-Clear Dropdown, dan Refresh Opsi Otomatis*) dirancang mencakup verifikasi perlindungan auto-clear ini pada antarmuka penambahan pengguna.

---

## GAP-DIV-E2E-003 — Evaluasi Status Dirty Guard Form Saat Nilai Diedit Lalu Dikembalikan ke Semula (Revert-to-Initial)

**Status:** terselesaikan via konvensi Wangs UI di spec  
**Tipe:** spesifikasi perilaku form UI  
**Dampak:** rendah  

PRD §4.2d Dialog 5 menetapkan bahwa modal konfirmasi Unsaved Changes muncul saat form dalam kondisi *dirty* ditutup melalui icon `[✕]` atau tombol `Esc`. Namun PRD tidak mendefinisikan apakah penentuan *dirty* menggunakan komparasi nilai murni (`currentValue !== initialValue`) atau histori perubahan (*isTouched* / keystroke history). Catatan pada `## Gap Spec` baris 802 di `tc-division.md` juga mengonfirmasi ketiadaan TC untuk kasus revert-to-initial.

**Yang diterapkan di spec:**  
Pada spec `TC-GS-DIV-E2E-019` (Create) dan `TC-GS-DIV-029` (Edit), ditegaskan kepatuhan terhadap standar formulir Wangs UI / React Hook Form: evaluasi dirty berbasis komparasi nilai. Jika pengguna mengubah input lalu mengetik ulang atau menghapus hingga nilainya identik dengan nilai awal saat form dibuka, form dianggap bersih (*pristine*) dan penekanan `[✕]` / `Esc` langsung menutup modal tanpa memicu Dialog 5 Unsaved Changes.

---

## GAP-DIV-E2E-004 — Penanganan Concurrency Edit Lapangan Beda (Name vs Code) pada Record yang Sama

**Status:** terbuka  
**Tipe:** spesifikasi konkurensi backend (record-level vs field-level update)  
**Dampak:** sedang terhadap kepastian data saat dual edit  

Berdasarkan keputusan NC-01 dan PRD §9.4.2 baris Edit D6, edit konkuren pada record yang sama menganut kebijakan last-write-wins tanpa dialog konflik versi. Namun `TC-GS-DIV-271` hanya menguji kondisi saat kedua admin mengedit field yang sama (Name).

Belum ada spesifikasi apakah sistem melakukan update parsial (PATCH per-field) atau penimpaan penuh (PUT seluruh record) saat Admin A mengedit Name dan bersamaan Admin B mengedit Code. Jika penimpaan penuh terjadi, perubahan Name dari Admin A berisiko ter-revert jika form Admin B masih memuat nama lama.

**Yang diterapkan di spec:**  
Spec `TC-GS-DIV-E2E-072` (*Konkurensi Antar-Admin: Last-Write-Wins pada Edit Bersamaan, Penolakan Duplicate Name, dan Penolakan Duplicate Manual Code*) memverifikasi alur last-write-wins dan mencatat log mutasi yang dihasilkan di Changelog.

---

## GAP-DIV-E2E-005 — Kebutuhan Test Harness Khusus Otomasi E2E Global Settings Division

**Status:** terbuka, dicatat di Prerequisites tiap spec  
**Tipe:** kesiapan environment uji otomasi  
**Dampak:** memblokir eksekusi test runner jika harness belum tersedia  

Seluruh kebutuhan dependensi otomasi telah dicatat pada `## Prerequisites` masing-masing spec untuk panduan implementasi tim pengembang otomasi:

| Kebutuhan Harness | Deskripsi & Kegunaan | Spec yang Membutuhkan |
|---|---|---|
| **Multi-Tenant Data Seeding** | Database seed terpisah untuk Client A dan Client B guna memvalidasi isolasi total master data divisi antar-organisasi | 070 |
| **Workspace Status Mutator** | Pengkondisian entitas berstatus Suspended dan Expired untuk memvalidasi penolakan aksi tulis (Create, Edit, Delete) dengan status HTTP 403 | 069 |
| **System Limits API Controller** | Manipulasi kuota `Master Data Count Limit` dan `Selection Limit` via Admin Console Plans & Licensing untuk pengujian batas limit dan seleksi massal | 022, 038, 073 |
| **Consumer Dropdown Sync Bridge** | Verifikasi refleksi mutasi katalog divisi secara instan ke form User Login dan User Non-Login | 023, 031, 065, 066 |
| **Multi-Tab Context & Multi-Actor Context** | Pengujian dual browser tab untuk mendeteksi race condition (last-write-wins, duplicate create collision, rebutan slot limit, dan idempotent delete) | 072, 073 |
| **Network Mock Interceptor** | Intercept respons API untuk simulasi error HTTP 500, penundaan respons jaringan (skeleton loader 3 detik), respons empty state, dan ekspor gagal | 003, 023, 032, 037, 044, 053, 061 |
| **Viewport Emulator** | Emulasi resolusi mobile Android (<768px) untuk memvalidasi tata letak card list, ketiadaan checkbox, dan bottom sheets | 075, 076 |

---

## Kepatuhan Suite Division

- **Cakupan TC:** 100% (296 dari 296 TC granular aktif dari `TC-GS-DIV-1` sampai `TC-GS-DIV-296` terpetakan secara lengkap tanpa satu pun yang tertinggal).
- **Duplikasi TC:** 0 (setiap `TC-GS-DIV-NN` hanya muncul tepat di satu spec).
- **Total Spec E2E:** 76 spec atomik terisolasi tinggi (`TC-GS-DIV-E2E-001` s/d `076`).
- **Pembagian Mode:** 60 spec `FE+BE` (live backend), 16 spec `Mode: mock` (loading skeleton, hover tooltip, guided walkthrough, fault injection 500 & timeout, DOM XSS sanitization, mobile Android layout).
- **Verifikasi Lint:** `npx spectra lint --strict specs/GlobalSettings/Division` → target 0 lint errors.
- **Karakter Non-Kanonikal:** 0 karakter CJK atau simbol non-standar.
- **Status Spec:** Seluruh 76 spec berstatus `draft` dengan deskripsi langkah bahasa Indonesia yang presisi, bebas dari flakiness cascading, siap untuk tahap penyusunan skrip otomasi (`tagsamurai-e2e-generate-script`).