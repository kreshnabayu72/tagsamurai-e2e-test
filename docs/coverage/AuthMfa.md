# Coverage E2E — Auth > MFA (Multi-Factor Authentication)

Sumber: `auth/mfa/TestCases/tc-mfa.md` (95 TC aktif), `auth/mfa/TestCases/tc-mfa-frontend.md` (58 case FE), dan `auth/mfa/TestCases/tc-mfa-backend.md`.
Suite: `specs/Auth/Mfa/`.
Prefix Modul: `AUTH` + `MFA` (`TC-AUTH-MFA-E2E-*`).
Status semua spec: `draft`.

**Aturan seleksi (2026-09-30):** Spec e2e merangkap TC FE. Semua TC masuk spec kecuali yang hanya-BE (validasi database/kontrak API internal murni). Kasus hanya-FE ditandai `Mode: mock`.
**Aturan granularitas:** Mengikuti standar granularitas tinggi di `specs/GlobalSettings/User` dan `specs/Auth/LoginOtp` — setiap spec atomik menguji satu topik aksi terisolasi, satu kondisi data / akun uji spesifik, dan memisahkan pengujian mekanik UI, boundary, timer, konkurensi, serta kegagalan server.

---

## 1. Pemetaan TC Granular & TC FE → Spec E2E (62 Spec)

| Spec E2E | Judul / Isi Skenario | Mode | TC Granular Sumber | TC FE (`tc-mfa-frontend.md`) |
|---|---|:---:|---|:---:|
| TC-AUTH-MFA-E2E-001 | Single-step login tanpa kondisi MFA terpicu langsung menghasilkan sesi penuh | FE+BE | TC-AUTH-MFA-1, 4 | TC-AUTH-MFA-FE-01 |
| TC-AUTH-MFA-E2E-002 | Pemicu MFA karena login pertama kali dan pembentukan pre-auth session | FE+BE | TC-AUTH-MFA-2, 7 | TC-AUTH-MFA-FE-02 |
| TC-AUTH-MFA-E2E-003 | Pemicu MFA karena idle 30 hari atau lebih sejak logout terakhir | FE+BE | TC-AUTH-MFA-3 | TC-AUTH-MFA-FE-03 |
| TC-AUTH-MFA-E2E-004 | Deteksi anomali login memicu MFA dan pengiriman email alert | FE+BE | TC-AUTH-MFA-5 | TC-AUTH-MFA-FE-04 |
| TC-AUTH-MFA-E2E-005 | Evaluasi idle 30 hari dihitung secara independen per platform web dan mobile | FE+BE | TC-AUTH-MFA-6 | TC-AUTH-MFA-FE-05 |
| TC-AUTH-MFA-E2E-006 | Device dikenal tidak memicu MFA sedangkan device baru memicu MFA dan email alert | FE+BE | TC-AUTH-MFA-8, 9 | TC-AUTH-MFA-FE-06 |
| TC-AUTH-MFA-E2E-007 | Pencocokan device exact match bukan similarity score | FE+BE | TC-AUTH-MFA-10 | TC-AUTH-MFA-FE-07 |
| TC-AUTH-MFA-E2E-008 | Pembersihan cookies atau storage browser terdeteksi sebagai device baru | FE+BE | TC-AUTH-MFA-11 | TC-AUTH-MFA-FE-08 |
| TC-AUTH-MFA-E2E-009 | Deteksi device baru tidak fail open saat layanan Geo-IP eksternal down | FE+BE | TC-AUTH-MFA-12 | TC-AUTH-MFA-FE-09 |
| TC-AUTH-MFA-E2E-010 | Lokasi login dalam radius 100km lolos dan jarak lebih dari 100km memicu MFA | FE+BE | TC-AUTH-MFA-13, 14 | TC-AUTH-MFA-FE-10 |
| TC-AUTH-MFA-E2E-011 | Negara sama tidak memicu MFA sedangkan perpindahan negara memicu MFA | FE+BE | TC-AUTH-MFA-15, 16 | TC-AUTH-MFA-FE-11 |
| TC-AUTH-MFA-E2E-012 | Penanganan kegagalan layanan Geo-IP dengan fail open untuk dimensi lokasi | mock | TC-AUTH-MFA-17 | TC-AUTH-MFA-FE-12 |
| TC-AUTH-MFA-E2E-013 | Siklus Country Pair Trust dari pasangan baru akumulasi frekuensi hingga decay | FE+BE | TC-AUTH-MFA-19, 20, 21, 22 | TC-AUTH-MFA-FE-13 |
| TC-AUTH-MFA-E2E-014 | Status trust negara tidak otomatis meloloskan anomali device baru atau jarak jauh | FE+BE | TC-AUTH-MFA-25 | TC-AUTH-MFA-FE-14 |
| TC-AUTH-MFA-E2E-015 | Screening layar Choose Method seleksi kartu opsi dan pengiriman kode OTP via email | FE+BE | TC-AUTH-MFA-26, 28, 29 | TC-AUTH-MFA-FE-15 |
| TC-AUTH-MFA-E2E-016 | Pemilihan metode Authenticator pada user yang sudah enroll langsung ke verifikasi | FE+BE | TC-AUTH-MFA-30 | TC-AUTH-MFA-FE-16 |
| TC-AUTH-MFA-E2E-017 | Pemilihan metode Authenticator pada user belum enroll diarahkan ke layar pendaftaran | FE+BE | TC-AUTH-MFA-31 | TC-AUTH-MFA-FE-17 |
| TC-AUTH-MFA-E2E-018 | Login Faktor-1 via OTP melewati layar Choose Method langsung ke Authenticator | FE+BE | TC-AUTH-MFA-27 | TC-AUTH-MFA-FE-18 |
| TC-AUTH-MFA-E2E-019 | Keseragaman tampilan layar Choose Method lintas berbagai pemicu MFA | FE+BE | TC-AUTH-MFA-32, 33 | TC-AUTH-MFA-FE-19 |
| TC-AUTH-MFA-E2E-020 | Verifikasi OTP kode salah expired lalu kode benar memicu auto-submit sukses | FE+BE | TC-AUTH-MFA-34, 35, 36 | TC-AUTH-MFA-FE-20 |
| TC-AUTH-MFA-E2E-021 | Validasi kode OTP kosong via tombol fallback Verify setelah error jaringan | mock | TC-AUTH-MFA-37 | TC-AUTH-MFA-FE-21 |
| TC-AUTH-MFA-E2E-022 | Kode OTP MFA lama invalid setelah alamat email akun diubah pada sesi lain | FE+BE | TC-AUTH-MFA-38 | TC-AUTH-MFA-FE-22 |
| TC-AUTH-MFA-E2E-023 | Kebijakan resend kode OTP pada MFA dengan cooldown dan batas kuota sesi | FE+BE | TC-AUTH-MFA-39 | TC-AUTH-MFA-FE-23 |
| TC-AUTH-MFA-E2E-024 | Navigasi Use a different method kembali ke Choose Method dan invalidate OTP aktif | FE+BE | TC-AUTH-MFA-40 | TC-AUTH-MFA-FE-24 |
| TC-AUTH-MFA-E2E-025 | Verifikasi kode Authenticator tanpa auto submit validasi kode salah dan login sukses | FE+BE | TC-AUTH-MFA-41, 42, 43, 45, 47 | TC-AUTH-MFA-FE-25 |
| TC-AUTH-MFA-E2E-026 | Toleransi drift window kode TOTP diterima dalam batas pergeseran waktu 1 step | FE+BE | TC-AUTH-MFA-44 | TC-AUTH-MFA-FE-26 |
| TC-AUTH-MFA-E2E-027 | Alur setup pendaftaran Authenticator Step 1 dan Step 2 hingga aktivasi inline | FE+BE | TC-AUTH-MFA-48, 49, 50, 51, 52 | TC-AUTH-MFA-FE-27 |
| TC-AUTH-MFA-E2E-028 | Penanganan kondisi balapan enrollment dari dua perangkat secara simultan | FE+BE | TC-AUTH-MFA-53 | TC-AUTH-MFA-FE-28 |
| TC-AUTH-MFA-E2E-029 | Retry permintaan enrollment dengan pre auth session sama bersifat idempoten | FE+BE | TC-AUTH-MFA-55 | TC-AUTH-MFA-FE-29 |
| TC-AUTH-MFA-E2E-030 | Pendaftaran Authenticator wajib dari kedua jalur masuk Choose Method dan Login OTP | FE+BE | TC-AUTH-MFA-56 | TC-AUTH-MFA-FE-30 |
| TC-AUTH-MFA-E2E-031 | Login berikutnya dari device dan lokasi yang telah trusted tidak memicu MFA | FE+BE | TC-AUTH-MFA-60 | TC-AUTH-MFA-FE-31 |
| TC-AUTH-MFA-E2E-032 | Status trusted device dievaluasi secara independen per platform web dan mobile | FE+BE | TC-AUTH-MFA-61 | TC-AUTH-MFA-FE-32 |
| TC-AUTH-MFA-E2E-033 | Pengiriman async email alert unusual login tanpa memblokir alur verifikasi MFA | FE+BE | TC-AUTH-MFA-68 | TC-AUTH-MFA-FE-33 |
| TC-AUTH-MFA-E2E-034 | Tombol Reset Password pada email alert mengarah ke form request reset normal | FE+BE | TC-AUTH-MFA-70 | TC-AUTH-MFA-FE-34 |
| TC-AUTH-MFA-E2E-035 | State CTA disabled label seragam Login dan loading guard double submit | FE+BE | TC-AUTH-MFA-71, 72, 73 | TC-AUTH-MFA-FE-35 |
| TC-AUTH-MFA-E2E-036 | Pencatatan login final sukses ke kedua surface tanpa duplikasi dan IP tercatat | FE+BE | TC-AUTH-MFA-74, 77, 78, 83 | TC-AUTH-MFA-FE-36 |
| TC-AUTH-MFA-E2E-037 | Note login final di kedua surface mencatat Login with OTP saat faktor pertama OTP | FE+BE | TC-AUTH-MFA-75 | TC-AUTH-MFA-FE-37 |
| TC-AUTH-MFA-E2E-038 | Note login final di kedua surface mencatat Login with biometric saat relogin mobile | FE+BE | TC-AUTH-MFA-76 | TC-AUTH-MFA-FE-38 |
| TC-AUTH-MFA-E2E-039 | Pencatatan kegagalan faktor kedua ke kedua surface sesuai enum Note spesifik | FE+BE | TC-AUTH-MFA-79 | TC-AUTH-MFA-FE-39 |
| TC-AUTH-MFA-E2E-040 | Peniadaan pencatatan log audit untuk aksi pendaftaran atau aktivasi Authenticator | FE+BE | TC-AUTH-MFA-80 | TC-AUTH-MFA-FE-40 |
| TC-AUTH-MFA-E2E-041 | Peniadaan pencatatan log audit untuk aksi resend OTP dalam konteks MFA | FE+BE | TC-AUTH-MFA-81 | TC-AUTH-MFA-FE-41 |
| TC-AUTH-MFA-E2E-042 | Sesi pre auth MFA kedaluwarsa setelah 10 menit membatalkan sesi dan redirect login | FE+BE | TC-AUTH-MFA-84 | TC-AUTH-MFA-FE-42 |
| TC-AUTH-MFA-E2E-043 | Sesi pre auth MFA yang telah digunakan tidak dapat dipakai ulang untuk login kedua | FE+BE | TC-AUTH-MFA-85 | TC-AUTH-MFA-FE-43 |
| TC-AUTH-MFA-E2E-044 | Batasan satu sesi pre auth aktif per user dan platform membatalkan sesi lama | FE+BE | TC-AUTH-MFA-86 | TC-AUTH-MFA-FE-44 |
| TC-AUTH-MFA-E2E-045 | Penanganan akun dinonaktifkan atau dihapus admin di tengah proses verifikasi MFA | FE+BE | TC-AUTH-MFA-87, 88 | TC-AUTH-MFA-FE-45 |
| TC-AUTH-MFA-E2E-046 | Proteksi balapan double submit atau auto submit ganda pada verifikasi faktor kedua | FE+BE | TC-AUTH-MFA-89 | TC-AUTH-MFA-FE-46 |
| TC-AUTH-MFA-E2E-047 | Penanganan retry submit verifikasi faktor kedua setelah network timeout client | mock | TC-AUTH-MFA-90 | TC-AUTH-MFA-FE-47 |
| TC-AUTH-MFA-E2E-048 | Penanganan kegagalan server 500 saat verifikasi faktor kedua dan toast error retry | mock | TC-AUTH-MFA-91 | TC-AUTH-MFA-FE-48 |
| TC-AUTH-MFA-E2E-049 | Retry evaluasi kebutuhan MFA pasca timeout bersifat idempoten | mock | TC-AUTH-MFA-92 | TC-AUTH-MFA-FE-49 |
| TC-AUTH-MFA-E2E-050 | Retry permintaan pendaftaran Authenticator mengembalikan respons QR dan rahasia identik | FE+BE | TC-AUTH-MFA-93 | TC-AUTH-MFA-FE-50 |
| TC-AUTH-MFA-E2E-051 | Kondisi balapan simultan verifikasi OTP Tab A vs verifikasi Authenticator Tab B | FE+BE | TC-AUTH-MFA-121 | TC-AUTH-MFA-FE-51 |
| TC-AUTH-MFA-E2E-052 | Kondisi balapan simultan verifikasi setup enrollment Tab A vs verifikasi OTP Tab B | FE+BE | TC-AUTH-MFA-122 | TC-AUTH-MFA-FE-52 |
| TC-AUTH-MFA-E2E-053 | Akses langsung via URL ke rute faktor kedua tanpa sesi pre auth diredirect ke login | FE+BE | TC-AUTH-MFA-95 | TC-AUTH-MFA-FE-53 |
| TC-AUTH-MFA-E2E-054 | Frontend tidak mengasumsikan status login sukses tanpa konfirmasi server resmi | mock | TC-AUTH-MFA-98 | TC-AUTH-MFA-FE-54 |
| TC-AUTH-MFA-E2E-055 | Aksesibilitas keyboard fokus otomatis aria describedby teks alternatif QR dan role radio | mock | TC-AUTH-MFA-110, 111, 112, 113 | TC-AUTH-MFA-FE-55 |
| TC-AUTH-MFA-E2E-056 | Reset Password modul lain tidak mereset trusted device enrollment maupun first login | FE+BE | TC-AUTH-MFA-117, 118 | TC-AUTH-MFA-FE-56 |
| TC-AUTH-MFA-E2E-057 | Status keaktifan user dibaca secara real time saat verifikasi faktor kedua | FE+BE | TC-AUTH-MFA-119 | TC-AUTH-MFA-FE-57 |
| TC-AUTH-MFA-E2E-058 | Fitur MFA berlaku identik di seluruh tier lisensi plan tanpa opsi penonaktifan | FE+BE | TC-AUTH-MFA-120 | TC-AUTH-MFA-FE-58 |
| TC-AUTH-MFA-E2E-059 | Nilai batas jarak anomali lokasi tepat 100km konsisten dengan ambang deteksi | mock | TC-AUTH-MFA-18 | — *(Manual di FE doc)* |
| TC-AUTH-MFA-E2E-060 | Tampilan mobile responsive halaman MFA layout vertikal dan keyboard angka | mock | TC-AUTH-MFA-114, 115 | — *(Manual di FE doc)* |
| TC-AUTH-MFA-E2E-061 | Login final via MFA menyerahkan evaluasi batas sesi konkuren ke Session Management | FE+BE | TC-AUTH-MFA-116 | — *(Manual di FE doc)* |
| TC-AUTH-MFA-E2E-062 | Kolom Device atau Browser pada entri log login final tercatat dalam format kanonikal | FE+BE | TC-AUTH-MFA-123 | — *(Gap-fill GAP-178)* |

---

## 2. Alasan TC Hanya-BE (Tidak Masuk Spec E2E)

1 TC tidak masuk ke dalam suite E2E karena menguji transaksi database atomik (fault injection rollback DB) murni tanpa keterlibatan antarmuka pengguna:

| TC ID | Skenario | Alasan Tidak Masuk Spec E2E |
|---|---|---|
| TC-AUTH-MFA-82 | Penulisan atomik — gagal tulis log → rollback | Menguji transaksi database atomik (DB failure injection) dan rollback sesi; diuji langsung di level backend API test (`tc-mfa-backend.md`). |

---

## 3. Lapisan per TC (Seluruh 95 TC Granular)

| TC ID | Skenario | Prioritas | Lapisan | Spec E2E | Mode | TC FE Ref (`tc-mfa-frontend.md`) | Catatan |
|---|---|:---:|:---:|---|:---:|:---:|---|
| TC-AUTH-MFA-1 | Happy path — tidak ada kondisi MFA terpenuhi | P0 | E2E | TC-AUTH-MFA-E2E-001 | FE+BE | TC-AUTH-MFA-FE-01 |  |
| TC-AUTH-MFA-2 | Login pertama (`first_login_at IS NULL`) | P0 | E2E | TC-AUTH-MFA-E2E-002 | FE+BE | TC-AUTH-MFA-FE-02 |  |
| TC-AUTH-MFA-3 | Idle ≥30 hari sejak logout terakhir (per platform) | P0 | E2E | TC-AUTH-MFA-E2E-003 | FE+BE | TC-AUTH-MFA-FE-03 |  |
| TC-AUTH-MFA-4 | Idle <30 hari — tidak memicu dimensi ini | P1 | E2E | TC-AUTH-MFA-E2E-001 | FE+BE | TC-AUTH-MFA-FE-01 |  |
| TC-AUTH-MFA-5 | Login tak biasa (device baru/lokasi/negara) memicu MFA | P0 | E2E | TC-AUTH-MFA-E2E-004 | FE+BE | TC-AUTH-MFA-FE-04 |  |
| TC-AUTH-MFA-6 | Idle ≥30 hari dihitung independen per platform | P1 | E2E | TC-AUTH-MFA-E2E-005 | FE+BE | TC-AUTH-MFA-FE-05 |  |
| TC-AUTH-MFA-7 | Faktor-1 tidak membuat sesi penuh saat MFA wajib | P0 | E2E | TC-AUTH-MFA-E2E-002 | FE+BE | TC-AUTH-MFA-FE-02 |  |
| TC-AUTH-MFA-8 | Device baru (`device_id` tidak ditemukan di `trusted_device`) | P0 | E2E | TC-AUTH-MFA-E2E-006 | FE+BE | TC-AUTH-MFA-FE-06 |  |
| TC-AUTH-MFA-9 | Device dikenal (`device_id` exact-match) — tidak memicu | P0 | E2E | TC-AUTH-MFA-E2E-006 | FE+BE | TC-AUTH-MFA-FE-06 |  |
| TC-AUTH-MFA-10 | Exact-match, bukan similarity — `device_id` sedikit berbeda tetap dianggap device baru | P1 | E2E | TC-AUTH-MFA-E2E-007 | FE+BE | TC-AUTH-MFA-FE-07 |  |
| TC-AUTH-MFA-11 | User clear cookies/reinstall app → dianggap device baru (by design) | P2 | E2E | TC-AUTH-MFA-E2E-008 | FE+BE | TC-AUTH-MFA-FE-08 |  |
| TC-AUTH-MFA-12 | Deteksi device baru TIDAK fail-open saat geo-IP service down | P1 | E2E | TC-AUTH-MFA-E2E-009 | FE+BE | TC-AUTH-MFA-FE-09 |  |
| TC-AUTH-MFA-13 | Lokasi >100km dari login terakhir (Haversine) | P0 | E2E | TC-AUTH-MFA-E2E-010 | FE+BE | TC-AUTH-MFA-FE-10 |  |
| TC-AUTH-MFA-14 | Lokasi ≤100km — tidak memicu dimensi ini | P0 | E2E | TC-AUTH-MFA-E2E-010 | FE+BE | TC-AUTH-MFA-FE-10 |  |
| TC-AUTH-MFA-15 | Beda negara (walau <100km) memicu MFA | P0 | E2E | TC-AUTH-MFA-E2E-011 | FE+BE | TC-AUTH-MFA-FE-11 |  |
| TC-AUTH-MFA-16 | Negara sama — tidak memicu dimensi ini | P0 | E2E | TC-AUTH-MFA-E2E-011 | FE+BE | TC-AUTH-MFA-FE-11 |  |
| TC-AUTH-MFA-17 | Geo-IP service down → fail-open | P1 | E2E | TC-AUTH-MFA-E2E-012 | mock | TC-AUTH-MFA-FE-12 |  |
| TC-AUTH-MFA-18 | Boundary — jarak tepat/mendekati 100km | P2 | E2E | TC-AUTH-MFA-E2E-059 | mock | — |  |
| TC-AUTH-MFA-19 | Pasangan negara baru — belum trusted | P0 | E2E | TC-AUTH-MFA-E2E-013 | FE+BE | TC-AUTH-MFA-FE-13 |  |
| TC-AUTH-MFA-20 | Pasangan mencapai `frequency=3` dalam 90 hari → trusted | P0 | E2E | TC-AUTH-MFA-E2E-013 | FE+BE | TC-AUTH-MFA-FE-13 |  |
| TC-AUTH-MFA-21 | `frequency<3` — tetap belum trusted | P1 | E2E | TC-AUTH-MFA-E2E-013 | FE+BE | TC-AUTH-MFA-FE-13 |  |
| TC-AUTH-MFA-22 | Decay — pasangan tidak muncul >180 hari | P1 | E2E | TC-AUTH-MFA-E2E-013 | FE+BE | TC-AUTH-MFA-FE-13 |  |
| TC-AUTH-MFA-25 | Trust negara TIDAK otomatis meloloskan dimensi device/jarak | P0 | E2E | TC-AUTH-MFA-E2E-014 | FE+BE | TC-AUTH-MFA-FE-14 |  |
| TC-AUTH-MFA-26 | Faktor-1 = Password, MFA wajib → tampil halaman pilihan | P0 | E2E | TC-AUTH-MFA-E2E-015 | FE+BE | TC-AUTH-MFA-FE-15 |  |
| TC-AUTH-MFA-27 | Faktor-1 = OTP → SKIP halaman pilihan | P0 | E2E | TC-AUTH-MFA-E2E-018 | FE+BE | TC-AUTH-MFA-FE-18 |  |
| TC-AUTH-MFA-28 | Pilih salah satu opsi → highlight & CTA enabled | P1 | E2E | TC-AUTH-MFA-E2E-015 | FE+BE | TC-AUTH-MFA-FE-15 |  |
| TC-AUTH-MFA-29 | Pilih "OTP via email" → navigate & kirim kode | P0 | E2E | TC-AUTH-MFA-E2E-015 | FE+BE | TC-AUTH-MFA-FE-15 |  |
| TC-AUTH-MFA-30 | Pilih "Authenticator app", sudah enroll | P0 | E2E | TC-AUTH-MFA-E2E-016 | FE+BE | TC-AUTH-MFA-FE-16 |  |
| TC-AUTH-MFA-31 | Pilih "Authenticator app", belum enroll | P0 | E2E | TC-AUTH-MFA-E2E-017 | FE+BE | TC-AUTH-MFA-FE-17 |  |
| TC-AUTH-MFA-32 | Halaman Choose Method seragam lintas semua `mfaReason` | P1 | E2E | TC-AUTH-MFA-E2E-019 | FE+BE | TC-AUTH-MFA-FE-19 |  |
| TC-AUTH-MFA-33 | `mfaReason` informational-only — tidak mengubah opsi yang ditawarkan | P2 | E2E | TC-AUTH-MFA-E2E-019 | FE+BE | TC-AUTH-MFA-FE-19 |  |
| TC-AUTH-MFA-34 | Kode benar (auto-submit) → login final sukses | P0 | E2E | TC-AUTH-MFA-E2E-020 | FE+BE | TC-AUTH-MFA-FE-20 |  |
| TC-AUTH-MFA-35 | Kode salah | P0 | E2E | TC-AUTH-MFA-E2E-020 | FE+BE | TC-AUTH-MFA-FE-20 |  |
| TC-AUTH-MFA-36 | Kode expired (>5 menit) | P0 | E2E | TC-AUTH-MFA-E2E-020 | FE+BE | TC-AUTH-MFA-FE-20 |  |
| TC-AUTH-MFA-37 | Kode kosong — verify via fallback sebelum 6 digit | P1 | E2E | TC-AUTH-MFA-E2E-021 | mock | TC-AUTH-MFA-FE-21 |  |
| TC-AUTH-MFA-38 | Kode OTP MFA lama invalid setelah email akun diganti di sesi lain | P0 | E2E | TC-AUTH-MFA-E2E-022 | FE+BE | TC-AUTH-MFA-FE-22 |  |
| TC-AUTH-MFA-39 | Resend mengikuti kebijakan identik Login with OTP (1 menit aktif, maks 5×/sesi MFA, cooldown 10 menit setelah ke-5); button label `"Resend code"` | P1 | E2E | TC-AUTH-MFA-E2E-023 | FE+BE | TC-AUTH-MFA-FE-23 |  |
| TC-AUTH-MFA-40 | "Use a different method" → kembali ke Choose Verification Method (bukan edit email) | P1 | E2E | TC-AUTH-MFA-E2E-024 | FE+BE | TC-AUTH-MFA-FE-24 |  |
| TC-AUTH-MFA-41 | Halaman Authenticator Verification — judul, kode TOTP benar → login final sukses | P0 | E2E | TC-AUTH-MFA-E2E-025 | FE+BE | TC-AUTH-MFA-FE-25 |  |
| TC-AUTH-MFA-42 | Kode TOTP salah | P0 | E2E | TC-AUTH-MFA-E2E-025 | FE+BE | TC-AUTH-MFA-FE-25 |  |
| TC-AUTH-MFA-43 | Kode kosong — submit sebelum 6 digit | P1 | E2E | TC-AUTH-MFA-E2E-025 | FE+BE | TC-AUTH-MFA-FE-25 |  |
| TC-AUTH-MFA-44 | Kode dalam drift window ±1 step diterima | P1 | E2E | TC-AUTH-MFA-E2E-026 | FE+BE | TC-AUTH-MFA-FE-26 |  |
| TC-AUTH-MFA-45 | Kode di luar drift window ditolak | P1 | E2E | TC-AUTH-MFA-E2E-025 | FE+BE | TC-AUTH-MFA-FE-25 |  |
| TC-AUTH-MFA-47 | Tidak ada auto-submit — verifikasi manual via klik CTA | P1 | E2E | TC-AUTH-MFA-E2E-025 | FE+BE | TC-AUTH-MFA-FE-25 |  |
| TC-AUTH-MFA-48 | Step 1 — heading, QR code & secret key tampil | P0 | E2E | TC-AUTH-MFA-E2E-027 | FE+BE | TC-AUTH-MFA-FE-27 |  |
| TC-AUTH-MFA-49 | Button "Copy key" berfungsi | P1 | E2E | TC-AUTH-MFA-E2E-027 | FE+BE | TC-AUTH-MFA-FE-27 |  |
| TC-AUTH-MFA-50 | Step 2 — kode benar → aktif & lanjut login final | P0 | E2E | TC-AUTH-MFA-E2E-027 | FE+BE | TC-AUTH-MFA-FE-27 |  |
| TC-AUTH-MFA-51 | Step 2 — kode salah | P0 | E2E | TC-AUTH-MFA-E2E-027 | FE+BE | TC-AUTH-MFA-FE-27 |  |
| TC-AUTH-MFA-52 | Tidak auto-submit di Step 2 — perlu klik "Verify" eksplisit | P1 | E2E | TC-AUTH-MFA-E2E-027 | FE+BE | TC-AUTH-MFA-FE-27 |  |
| TC-AUTH-MFA-53 | Enrollment race — 2 device bersamaan | P1 | E2E | TC-AUTH-MFA-E2E-028 | FE+BE | TC-AUTH-MFA-FE-28 |  |
| TC-AUTH-MFA-55 | Retry enroll dgn `mfa_session` sama (network timeout) | P1 | E2E | TC-AUTH-MFA-E2E-029 | FE+BE | TC-AUTH-MFA-FE-29 |  |
| TC-AUTH-MFA-56 | Enrollment wajib saat memilih Authenticator & belum pernah enroll, dari kedua jalur (Choose Method / handoff OTP) | P1 | E2E | TC-AUTH-MFA-E2E-030 | FE+BE | TC-AUTH-MFA-FE-30 |  |
| TC-AUTH-MFA-60 | Login berikutnya dari device+lokasi trusted tidak memicu MFA by dimensi tsb | P0 | E2E | TC-AUTH-MFA-E2E-031 | FE+BE | TC-AUTH-MFA-FE-31 |  |
| TC-AUTH-MFA-61 | Trust per-platform independen | P1 | E2E | TC-AUTH-MFA-E2E-032 | FE+BE | TC-AUTH-MFA-FE-32 |  |
| TC-AUTH-MFA-68 | Pengiriman async, tidak memblok alur MFA | P1 | E2E | TC-AUTH-MFA-E2E-033 | FE+BE | TC-AUTH-MFA-FE-33 |  |
| TC-AUTH-MFA-70 | Tombol `[Reset Password]` mengarah ke halaman request (§6.3 `email-format.md`), bukan langsung Set Password | P2 | E2E | TC-AUTH-MFA-E2E-034 | FE+BE | TC-AUTH-MFA-FE-34 |  |
| TC-AUTH-MFA-71 | CTA label "Login" seragam di semua halaman MFA | P1 | E2E | TC-AUTH-MFA-E2E-035 | FE+BE | TC-AUTH-MFA-FE-35 |  |
| TC-AUTH-MFA-72 | Choose Method — CTA disabled sebelum memilih opsi | P1 | E2E | TC-AUTH-MFA-E2E-035 | FE+BE | TC-AUTH-MFA-FE-35 |  |
| TC-AUTH-MFA-73 | Loading state (double-submit guard) saat submit | P0 | E2E | TC-AUTH-MFA-E2E-035 | FE+BE | TC-AUTH-MFA-FE-35 |  |
| TC-AUTH-MFA-74 | Login final via MFA dicatat SEKALI, Note sesuai faktor pertama | P0 | E2E | TC-AUTH-MFA-E2E-036 | FE+BE | TC-AUTH-MFA-FE-36 |  |
| TC-AUTH-MFA-75 | Note mengikuti faktor-1 = OTP | P0 | E2E | TC-AUTH-MFA-E2E-037 | FE+BE | TC-AUTH-MFA-FE-37 |  |
| TC-AUTH-MFA-76 | Note mengikuti faktor-1 = Biometric Re-login (mobile) | P0 | E2E | TC-AUTH-MFA-E2E-038 | FE+BE | TC-AUTH-MFA-FE-38 |  |
| TC-AUTH-MFA-77 | Faktor-1 TIDAK menulis Success saat MFA terpicu (cegah double-Success) | P0 | E2E | TC-AUTH-MFA-E2E-036 | FE+BE | TC-AUTH-MFA-FE-36 |  |
| TC-AUTH-MFA-78 | Tidak ada duplikasi Success (double-Success check end-to-end) | P0 | E2E | TC-AUTH-MFA-E2E-036 | FE+BE | TC-AUTH-MFA-FE-36 |  |
| TC-AUTH-MFA-79 | Kegagalan faktor-2 dicatat sesuai enum Note | P0 | E2E | TC-AUTH-MFA-E2E-039 | FE+BE | TC-AUTH-MFA-FE-39 |  |
| TC-AUTH-MFA-80 | Enrollment/aktivasi Authenticator TIDAK dicatat | P0 | E2E | TC-AUTH-MFA-E2E-040 | FE+BE | TC-AUTH-MFA-FE-40 |  |
| TC-AUTH-MFA-81 | Resend OTP (dalam konteks MFA) TIDAK dicatat | P1 | E2E | TC-AUTH-MFA-E2E-041 | FE+BE | TC-AUTH-MFA-FE-41 |  |
| TC-AUTH-MFA-82 | Penulisan atomik — gagal tulis log → rollback | P0 | BE | — | — | — | DB transaction rollback (pure BE) |
| TC-AUTH-MFA-83 | IP Address tercatat pada entri login final | P1 | E2E | TC-AUTH-MFA-E2E-036 | FE+BE | TC-AUTH-MFA-FE-36 |  |
| TC-AUTH-MFA-123 | Device / Browser pada entri login final sesuai format kanonikal lintas produk (`GAP-178`) | P1 | E2E | TC-AUTH-MFA-E2E-062 | FE+BE | — |  |
| TC-AUTH-MFA-84 | `mfa_session` TTL 10 menit — expired | P0 | E2E | TC-AUTH-MFA-E2E-042 | FE+BE | TC-AUTH-MFA-FE-42 |  |
| TC-AUTH-MFA-85 | `mfa_session` sudah `is_consumed=true` tidak bisa dipakai ulang | P0 | E2E | TC-AUTH-MFA-E2E-043 | FE+BE | TC-AUTH-MFA-FE-43 |  |
| TC-AUTH-MFA-86 | Satu `mfa_session` aktif per `(user_id, platform)` | P1 | E2E | TC-AUTH-MFA-E2E-044 | FE+BE | TC-AUTH-MFA-FE-44 |  |
| TC-AUTH-MFA-87 | User di-deactivate saat MFA berlangsung | P0 | E2E | TC-AUTH-MFA-E2E-045 | FE+BE | TC-AUTH-MFA-FE-45 |  |
| TC-AUTH-MFA-88 | User di-delete saat MFA berlangsung | P1 | E2E | TC-AUTH-MFA-E2E-045 | FE+BE | TC-AUTH-MFA-FE-45 |  |
| TC-AUTH-MFA-89 | Double-submit / auto-submit race pada verify OTP/Authenticator | P0 | E2E | TC-AUTH-MFA-E2E-046 | FE+BE | TC-AUTH-MFA-FE-46 |  |
| TC-AUTH-MFA-90 | Retry verify setelah network timeout | P0 | E2E | TC-AUTH-MFA-E2E-047 | mock | TC-AUTH-MFA-FE-47 |  |
| TC-AUTH-MFA-91 | Network/5xx saat verify faktor-2 | P0 | E2E | TC-AUTH-MFA-E2E-048 | mock | TC-AUTH-MFA-FE-48 |  |
| TC-AUTH-MFA-92 | Retry `POST /auth/mfa/evaluate` setelah timeout | P1 | E2E | TC-AUTH-MFA-E2E-049 | mock | TC-AUTH-MFA-FE-49 |  |
| TC-AUTH-MFA-93 | Retry enroll dgn `mfa_session` sama (idempotent per token) | P1 | E2E | TC-AUTH-MFA-E2E-050 | FE+BE | TC-AUTH-MFA-FE-50 |  |
| TC-AUTH-MFA-121 | 8b-1: Cross-action race — Verify OTP vs Verify Authenticator bersamaan (`mfa_session` sama, 2 tab) | P0 | E2E | TC-AUTH-MFA-E2E-051 | FE+BE | TC-AUTH-MFA-FE-51 |  |
| TC-AUTH-MFA-122 | 8b-1: Cross-action race — Enrollment Verify vs Verify OTP bersamaan (2 jalur faktor-2 berbeda, `mfa_session` sama) | P0 | E2E | TC-AUTH-MFA-E2E-052 | FE+BE | TC-AUTH-MFA-FE-52 |  |
| TC-AUTH-MFA-95 | Faktor-2 tidak bisa diakses tanpa `mfa_session` valid | P0 | E2E | TC-AUTH-MFA-E2E-053 | FE+BE | TC-AUTH-MFA-FE-53 |  |
| TC-AUTH-MFA-98 | FE tidak menyimpulkan sukses tanpa konfirmasi server | P1 | E2E | TC-AUTH-MFA-E2E-054 | mock | TC-AUTH-MFA-FE-54 |  |
| TC-AUTH-MFA-110 | Semua field kode (OTP/TOTP) keyboard accessible, auto-focus field pertama | P1 | E2E | TC-AUTH-MFA-E2E-055 | mock | TC-AUTH-MFA-FE-55 |  |
| TC-AUTH-MFA-111 | Caption error terasosiasi via `aria-describedby` | P1 | E2E | TC-AUTH-MFA-E2E-055 | mock | TC-AUTH-MFA-FE-55 |  |
| TC-AUTH-MFA-112 | QR code enrollment punya alternatif teks utk screen reader / non-camera | P1 | E2E | TC-AUTH-MFA-E2E-055 | mock | TC-AUTH-MFA-FE-55 |  |
| TC-AUTH-MFA-113 | Option cards Choose Method pakai `role="radio"`/`role="radiogroup"` | P2 | E2E | TC-AUTH-MFA-E2E-055 | mock | TC-AUTH-MFA-FE-55 |  |
| TC-AUTH-MFA-114 | Layout mobile full-screen vertical di semua halaman MFA | P2 | E2E | TC-AUTH-MFA-E2E-060 | mock | — |  |
| TC-AUTH-MFA-115 | Keyboard angka langsung di mobile untuk field OTP/TOTP | P2 | E2E | TC-AUTH-MFA-E2E-060 | mock | — |  |
| TC-AUTH-MFA-116 | Login final via MFA memicu evaluasi Session Management | P2 | E2E | TC-AUTH-MFA-E2E-061 | FE+BE | — |  |
| TC-AUTH-MFA-117 | Reset Password (modul lain) TIDAK memengaruhi trust device / enrollment MFA | P0 | E2E | TC-AUTH-MFA-E2E-056 | FE+BE | TC-AUTH-MFA-FE-56 |  |
| TC-AUTH-MFA-118 | Reset Password TIDAK mereset `first_login_at` | P1 | E2E | TC-AUTH-MFA-E2E-056 | FE+BE | TC-AUTH-MFA-FE-56 |  |
| TC-AUTH-MFA-119 | Status user (Active/Deactivated) dibaca real-time dari GS > User, bukan cache | P0 | E2E | TC-AUTH-MFA-E2E-057 | FE+BE | TC-AUTH-MFA-FE-57 |  |
| TC-AUTH-MFA-120 | MFA berlaku identik lintas semua plan & entitas, tidak dapat dinonaktifkan | P1 | E2E | TC-AUTH-MFA-E2E-058 | FE+BE | TC-AUTH-MFA-FE-58 |  |
