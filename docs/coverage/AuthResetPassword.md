# Coverage E2E — Auth > Reset Password

Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (96 TC aktif). Suite: `specs/auth2/ResetPassword/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `npx spectra lint --strict specs/auth2/ResetPassword` → `✓ 29 specs and 1 suites verified. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, spec e2e merangkap TC FE. Semua TC masuk spec kecuali hanya-BE. Spec yang butuh kondisi terpicu (created via API, intercept, viewport mobile, simulasi buta warna) ditandai `Mode: mock`. Hambatan teknis dicatat di `Prerequisites`, bukan menjadi alasan mengeluarkan TC.

**Nomor folder.** Prefix `TC-AUTH-RST-E2E-` berasal dari `AUTH` + `RST` di `foundation/tc-prefix-registry.md`. Nomor adalah urutan spec, bukan nomor TC sumber, sehingga tidak sama dengan nomor TC granular.

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-RST-E2E-001 | Screening halaman permintaan, validasi Email, batas 120 karakter, trim spasi | 1, 4, 5, 6, 7, 8 | web |
| TC-AUTH-RST-E2E-002 | Tampilan responsif di mobile browser, reCAPTCHA tetap varian checkbox | 2 | web |
| TC-AUTH-RST-E2E-003 | Ketiadaan reCAPTCHA di native app dan submit tanpa captcha | 3 | **mobile** |
| TC-AUTH-RST-E2E-004 | Account status gate: belum terdaftar, Inactive, sudah dihapus, dan urutan evaluasi | 9, 10, 11, 12 | web |
| TC-AUTH-RST-E2E-005 | reCAPTCHA gate: submit tanpa token, submit dengan token, urutan terhadap format Email | 13, 14 | web |
| TC-AUTH-RST-E2E-006 | Request sukses, isi email, dan request baru meng-invalidasi token aktif sebelumnya | 15, 16 | web |
| TC-AUTH-RST-E2E-007 | Double-submit pada halaman permintaan dan halaman Setup New Password | 19, 65 | web |
| TC-AUTH-RST-E2E-008 | Retry setelah client timeout pada Request (cooldown) dan Submit (token satu kali pakai) | 66, 84, 85 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-009 | Kegagalan server pada Request, Resend, Validate, Submit, dan respons lambat tanpa asumsi sukses | 20, 25, 41, 63, 91 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-010 | Tampilan Email Sent, countdown Resend, fallback email kosong, navigasi Back to Login | 21, 22, 27, 118 | web |
| TC-AUTH-RST-E2E-011 | Resend berhasil, token lama di-invalidasi, resend normal tidak dicatat | 23, 24, 26 | web |
| TC-AUTH-RST-E2E-012 | Rate limit per email dengan penyamaran respons, quota tetap berlaku tanpa subjek, Request dan Resend berbagi counter | 28, 30, 86 | web |
| TC-AUTH-RST-E2E-013 | Rate limit per IP tidak dicatat, cooldown 60 detik, independensi dua lapisan | 31, 32, 33 | web |
| TC-AUTH-RST-E2E-014 | Token valid merender Setup New Password, validate read-only, dua tab membuka link sama | 35, 40, 87 | web |
| TC-AUTH-RST-E2E-015 | Empat kondisi token invalid dengan dua varian copy dan tanpa kebocoran penyebab | 36, 37, 38, 39, 70, 71, 74 | web |
| TC-AUTH-RST-E2E-016 | Navigasi CTA "Request New Link" dan "Go to Login" dari halaman 404 | 72, 73 | web |
| TC-AUTH-RST-E2E-017 | Checklist Password Policy real-time, batas 7 dan 73 karakter, tiap rule, spasi, show/hide, tanpa reCAPTCHA | 43, 45, 46, 47, 48, 49, 50, 51, 56, 57 | web |
| TC-AUTH-RST-E2E-018 | Validasi yang memblokir submit: Password kosong, Confirm kosong, tidak sama, sama dengan yang lama | 52, 53, 54, 55 | web |
| TC-AUTH-RST-E2E-019 | Submit diterima pada baris batas 8 dan 72 karakter | 42, 44 | web |
| TC-AUTH-RST-E2E-020 | Submit sukses, konsumsi token, submit sukses tercatat, identitas user tidak berubah | 58, 59, 80, 113 | web |
| TC-AUTH-RST-E2E-021 | Cross-module: reset sukses membersihkan lock Login dan meng-invalidasi sesi mobile | 111, 120 | web |
| TC-AUTH-RST-E2E-022 | Submit saat token expired, token sudah dipakai, dan penolakan policy server | 60, 61, 62, 81 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-023 | Tampilan halaman Password Reset Successful, navigasinya, dan buka ulang link | 67, 68, 69 | web |
| TC-AUTH-RST-E2E-024 | Race Submit versus Resend dan Submit versus Request baru | 115, 116 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-025 | Perubahan email yang dikonfirmasi meng-invalidasi seluruh token reset aktif | 112 | web |
| TC-AUTH-RST-E2E-026 | A11y: urutan fokus di dua halaman, ikon mata via keyboard, checklist tanpa warna, toast polite | 104, 105, 106, 107, 108 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-027 | Ketersediaan dan kesetaraan alur lintas tier plan | 114 | web |
| TC-AUTH-RST-E2E-028 | Request sukses tercatat di kedua surface, kolom IP Address, kolom Device / Browser | 75, 83, 119 | web |
| TC-AUTH-RST-E2E-029 | Pencatatan Inactive, Too many attempts, dan dua kondisi tidak-tercatat | 76, 77, 78, 79 | web |

Total: 96 dari 96 TC aktif tercakup, tanpa duplikasi. 28 spec web, 1 spec mobile, 6 spec `Mode: mock`.

## TC sumber yang tidak masuk spec

Tidak ada. Seluruh 96 TC aktif masuk spec e2e, termasuk TC yang ditandai `Manual Only` atau `FE Test: UI Only`.

| TC | Alasan |
|---|---|
| 17, 18, 29, 34, 64, 82, 88, 89, 90, 92, 103, 117 | Tidak lagi ada sebagai baris TC di file aktif. ID muncul hanya di catatan changelog atau catatan QA, bukan sebagai kasus uji |
| 94, 109, 110 | Tidak lagi ada sebagai baris TC di file aktif. `109` dan `110` dicabut pada changelog 2026-10-01 (mobile removal, web-only); `94` disebut pada catatan TODO PRD basi, bukan sebagai kasus uji |

Tidak ada file `tc-reset-password-backend.md`, jadi tidak ada TC hanya-BE yang perlu dikeluarkan. Kategori P (API Contract) di file sumber berisi 0 TC.

## Verifikasi silang

- Tidak ada `sourceTc` yang muncul di dua spec. Audit terhadap `sourceTc` seluruh spec melaporkan `DUPLICATE: none` dengan 96 ID unik.
- Semua 96 ID TC yang ada sebagai baris di file sumber tercakup, dan tidak ada `sourceTc` di spec yang tidak ada di file sumber.
- Nomor langkah tiap spec dimulai dari 1 dan berurutan tanpa lompatan.
- Semua judul berformat `... : ...` sudah diapit tanda kutip agar frontmatter YAML valid.

## Pola steady-state yang dipakai

Setiap spec mengikuti pola berikut supaya dapat dijalankan sendiri:

1. **Prerequisites** memuat seluruh kebutuhan sebagai sumber resmi bagi tim FE: role, data pre-setup, dan hook. Semua alur di modul ini bersifat publik atau tanpa login, jadi tidak ada Role Matrix.
2. **Seed data lewat hook.** Token expired, consumed, invalidated, dan aktif dibuat lewat API Global Settings > User pada `beforeEach`, dan user yang dikunci dikembalikan ke keadaan awal pada `afterEach`. Spec tidak saling menumpang hasil.
3. **Verifikasi state** dibaca dari sumber yang benar, bukan dari asumsi tampilan: status token dari helper token, tahap lock dan counter dari Global Settings > User, status sesi dari helper sesi, dan entri log dari kedua surface pencatatan auth.
4. **Counter limit bersama** untuk limit per email, limit per IP, dan cooldown 60 detik dikembalikan ke keadaan awal oleh hook, sehingga spec 012 dan 013 tidak bergantung pada spec 011 atau spec 006.
5. **Angka batas limit** masih catatan engineering di PRD. Spec 012 dan 013 mengirim request berulang sampai efek yang diamati muncul dan mencatat jumlah request-nya sebagai bahan konfirmasi, bukan mengasumsikan angka final.
6. **Nilai sensitif** tidak ada di spec maupun fixture. Password lewat `Spectra.env.AUTH_PASSWORD` dan `Spectra.env.AUTH_NEW_PASSWORD` sampai `_3`, kredensial admin lewat `Spectra.env.ADMIN_EMAIL` dan `Spectra.env.ADMIN_PASSWORD`, dan nilai token hanya dibaca lewat helper.
7. **Copy panjang** diambil dari `Fixture.authResetPassword.captions` dan label checklist dari `Fixture.authResetPassword.checklist`, sesuai e2e-conventions.md bagian 9.

## Keputusan yang perlu ditinjau

- `parallel: false` pada suite, karena lima spec saling memengaruhi: limit per IP dan per email pada spec 012 dan 013, status user serta lock pada spec 004, 020, dan 021, cooldown server-side pada spec 011 dan 013, dan mailbox uji bersama pada spec 006, 008, dan 011.
- `TC-AUTH-RST-107` berstatus `Manual Only` di TC granular. Sesuai e2e-conventions.md bagian 2 label tersebut bukan alasan mengeluarkan TC, dan simulasi buta warna di spec 026 diwujudkan lewat filter grayscale yang dicatat di Prerequisites.
- `TC-AUTH-RST-59` diuji sebagai satu user terkunci pada tahap requires reset, bukan diulang untuk keempat tahap lock. Yang diuji adalah bahwa submit yang berhasil melepas lock dari tahap apa pun, dan keempat tahap lock beserta eskalasinya sudah tercakup di suite `Auth Login with Password`.
- `TC-AUTH-RST-118` diuji lewat request yang konteks emailnya dibuat kosong, bukan lewat data rusak di sisi FE. Yang diuji adalah fallback teks generik, dan provisioning kondisi itu dicatat di Prerequisites.
- Race pada spec 024 tidak mengasumsikan request mana yang lebih dulu ter-commit. Yang diverifikasi adalah invarian: password hanya berubah satu kali atau tidak sama sekali, token berakhir pada satu status final, dan tidak pernah ada dua token aktif milik user yang sama.
- Spec 003 memakai `coverage.mobile` sesuai aturan bahwa TC mobile tetap diotomasikan. Spec 002 memakai viewport mobile pada target web karena TC sumber menyebut mobile browser, bukan native app, dan keduanya dipisahkan supaya perbedaan platformnya eksplisit.

## Berikutnya

Belum ada `web.test.ts`, fixture, step, maupun hook. Itu pekerjaan skill `tagsamurai-e2e-generate-script` dan tidak dikerjakan di tahap ini.