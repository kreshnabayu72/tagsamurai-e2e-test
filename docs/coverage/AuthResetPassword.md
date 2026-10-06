# Coverage E2E — Auth > Reset Password

Sumber: `auth/reset-password/TestCases/tc-reset-password.md` (137 TC aktif per 2026-10-06). Suite: `specs/Auth/ResetPassword/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `npx spectra lint --strict specs/Auth/ResetPassword` → `✓ 27 specs and 1 suites verified. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, spec e2e merangkap TC FE. Semua TC masuk spec kecuali hanya-BE. Modul Reset Password adalah modul pra-autentikasi publik dengan seluruh 137 TC memiliki relevansi langsung terhadap UI, alur navigasi, validasi klien/server, atau audit log (0 TC yang dikeluarkan). Spec yang butuh kondisi terpicu (intercept 500/timeout, rate limit IP, viewport mobile) ditandai `Mode: mock`. Hambatan teknis dicatat di `Prerequisites`, bukan menjadi alasan mengeluarkan TC.

**Nomor folder:** Prefix `TC-AUTH-RST-E2E-` berasal dari `AUTH` + `RST` di `foundation/tc-prefix-registry.md`. Nomor adalah urutan spec (`001`–`027`), bukan nomor TC sumber.

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-RST-E2E-001 | Screening halaman Reset Password, navigasi bolak-balik dengan Login, dan urutan fokus keyboard Tab | 01, 02, 03, 04, 05 | web |
| TC-AUTH-RST-E2E-002 | Validasi field Email pada halaman Request Reset: wajib diisi, format, batas karakter, dan payload injeksi | 13, 15, 16, 17, 18, 119, 128 | web |
| TC-AUTH-RST-E2E-003 | Evaluasi Google reCAPTCHA v2 pada halaman Request Reset: submit tanpa captcha, token expired, dan layanan tidak terjangkau | 19, 20, 21, 22, 120, 121 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-004 | Evaluasi akun saat Request Reset: email tidak terdaftar, akun dihapus, akun inactive, dan status Client | 23, 24, 25, 26, 27 | web |
| TC-AUTH-RST-E2E-005 | Request Reset Password sukses: loading spinner, penerbitan token baru, pengiriman email, dan navigasi ke Email Sent! | 12, 14, 28, 118 | web |
| TC-AUTH-RST-E2E-006 | Rate limiting per alamat IP pada halaman Request: penolakan 429 dan pemulihan jendela waktu | 35, 36, 37 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-007 | Pembatasan laju reset per email: cooldown 60 detik, kuota 5 kali per 24 jam, penyamaran respons, dan sliding window | 29, 30, 31, 32, 34, 38 | web |
| TC-AUTH-RST-E2E-008 | Screening halaman Email Sent!, countdown timer Resend, dan navigasi kembali | 39, 40, 41, 45, 51 | web |
| TC-AUTH-RST-E2E-009 | Halaman Email Sent! tanpa konteks email: fallback teks generik, section Resend tersembunyi, dan navigasi Back to Reset | 46 | web |
| TC-AUTH-RST-E2E-010 | Resend email reset setelah cooldown: pembatalan token lama, penerbitan token baru, dan toast sukses | 42, 43, 44, 57, 125 | web |
| TC-AUTH-RST-E2E-011 | Penolakan Resend Email: akun nonaktif, akun dihapus, kuota per email habis, dan budget bersama | 33, 47, 48, 49 | web |
| TC-AUTH-RST-E2E-012 | Validasi tautan token reset: pembukaan idempotent tanpa efek samping dan masa berlaku 24 jam | 54, 56, 58, 59 | web |
| TC-AUTH-RST-E2E-013 | Halaman 404 varian Expired: token kedaluwarsa 24 jam, akun nonaktif/dihapus, dan navigasi Request New Link | 52, 53, 55, 60, 61 | web |
| TC-AUTH-RST-E2E-014 | Screening halaman Setup New Password, state awal form, aksesibilitas ARIA, dan urutan keyboard | 63, 64, 65, 66, 70 | web |
| TC-AUTH-RST-E2E-015 | Evaluasi reaktif Password Policy checklist, batas karakter 8-72, dan karakter spesial | 67, 68, 69, 80 | web |
| TC-AUTH-RST-E2E-016 | Validasi form Setup New Password: field wajib diisi, konfirmasi cocok, penolakan policy server, dan spasi | 71, 72, 73, 74, 75, 76, 77, 78, 122, 124 | web |
| TC-AUTH-RST-E2E-017 | Penolakan password baru sama dengan password aktif saat ini | 79, 123 | web |
| TC-AUTH-RST-E2E-018 | Submit New Password sukses, navigasi login, konsumsi token sekali pakai, dan Halaman 404 Already Used | 81, 82, 83, 84, 85, 86, 127 | web |
| TC-AUTH-RST-E2E-019 | Verifikasi login dengan password baru, penolakan password lama, sifat case-sensitive, dan pengakhiran sesi aktif | 111, 112, 113 | web |
| TC-AUTH-RST-E2E-020 | Pemulihan status terkunci (15 menit, 1 jam, Requires Reset, dan Permanen) melalui Reset Password sukses | 106, 107, 108, 109, 110, 116, 117 | web |
| TC-AUTH-RST-E2E-021 | Ketahanan terhadap gangguan server 5xx dan timeout pada alur Request, Resend, Validate Link, dan Submit | 50, 62, 87, 88, 90, 91, 92 | web (`Mode: mock`) |
| TC-AUTH-RST-E2E-022 | Pencegahan double-submit dan penanganan race condition antar tab browser | 89, 93, 129, 130 | web |
| TC-AUTH-RST-E2E-023 | Perubahan state user di tengah alur: konfirmasi ubah email, user dinonaktifkan, dan token expired saat form terbuka | 114, 115, 131, 132, 133 | web |
| TC-AUTH-RST-E2E-024 | Pencatatan audit log di dua surface (Activity Log > Session dan User Log): event sukses, event gagal, dan atribut entri | 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 134, 135, 136 | web |
| TC-AUTH-RST-E2E-025 | Verifikasi kondisi yang tidak dicatat pada audit log: email tidak terdaftar, kesalahan input field, submit token tidak dikenal, dan Resend sukses | 104, 105, 126, 137 | web |
| TC-AUTH-RST-E2E-026 | Perilaku akses halaman Reset Password dan tautan token oleh user yang telah memiliki sesi aktif | 10, 11 | web |
| TC-AUTH-RST-E2E-027 | Alur Reset Password pada aplikasi native Android: ketiadaan reCAPTCHA dan penanganan App Link | 06, 07, 08, 09 | mobile (`Mode: mock`) |

Total: **137 dari 137 TC aktif tercakup 100% tanpa celah dan tanpa duplikasi.**
(23 spec Web FE+BE, 3 spec Web Mock, 1 spec Mobile Mock).

## TC sumber yang tidak masuk spec

Tidak ada (0 TC). Seluruh 137 TC granular memiliki manifestasi UI, validasi klien/server, navigasi, atau pencatatan audit log yang diuji dalam rangkaian spec ini.

## Verifikasi silang

- Tidak ada `sourceTc` yang muncul di dua spec (seluruh 137 ID unik terpetakan tepat 1-to-1).
- Format penamaan direktori dan frontmatter YAML telah divalidasi linter TestSpectra.
