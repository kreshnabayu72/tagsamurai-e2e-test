# Coverage E2E — Auth > Login with OTP

Sumber: `auth/login-otp/TestCases/tc-login-otp.md` (101 TC aktif) dan `auth/login-otp/TestCases/tc-login-otp-backend.md`.
Suite: `specs/Auth/LoginOtp/`.
Prefix Modul: `AUTH` + `OTP` (`TC-AUTH-OTP-E2E-*`).
Status semua spec: `draft`.

**Aturan seleksi (2026-09-30):** Spec e2e merangkap TC FE. Semua TC masuk spec kecuali yang hanya-BE (validasi database/kontrak API internal murni). Kasus hanya-FE ditandai `Mode: mock`.
**Aturan granularitas:** Mengikuti standar granularitas tinggi di `specs/GlobalSettings/User` — setiap spec atomik menguji satu topik aksi terisolasi, satu kondisi data / akun uji spesifik, dan memisahkan pengujian mekanik UI, boundary, timer, konkurensi, serta kegagalan server.

---

## 1. Pemetaan TC Granular → Spec E2E (45 Spec Terurut Kronologis)

### Fase 1: Halaman Input Email (Screening, Navigasi, Validasi, Blokir Status, Mock Error, Mobile)
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-001 | Screening form Input Email Login with OTP | FE+BE | TC-AUTH-OTP-1, 97 |
| TC-AUTH-OTP-E2E-002 | Navigasi bolak-balik Login Password dan Login OTP dengan persistensi prefilled email | FE+BE | TC-AUTH-OTP-3, 67 |
| TC-AUTH-OTP-E2E-003 | Validasi format field Email pada Request OTP (kosong, format salah, 120 char boundary, auto-trim, aria-describedby) | FE+BE | TC-AUTH-OTP-5, 6, 9, 10, 71, 95 |
| TC-AUTH-OTP-E2E-004 | Validasi email belum terdaftar dan proteksi reCAPTCHA gate belum diselesaikan | FE+BE | TC-AUTH-OTP-7, 11, 71 |
| TC-AUTH-OTP-E2E-005 | Request OTP berhasil dengan panjang karakter email tepat 120 karakter (nilai batas maksimum) | FE+BE | TC-AUTH-OTP-8 |
| TC-AUTH-OTP-E2E-006 | Request OTP diblokir untuk akun berstatus Pending Activation | FE+BE | TC-AUTH-OTP-23, 70 |
| TC-AUTH-OTP-E2E-007 | Request OTP diblokir untuk akun berstatus Inactive | FE+BE | TC-AUTH-OTP-24, 70 |
| TC-AUTH-OTP-E2E-008 | Request OTP untuk akun terhapus diblokir dengan proteksi anti-enumeration | FE+BE | TC-AUTH-OTP-101, 71 |
| TC-AUTH-OTP-E2E-009 | Request OTP diblokir saat akun dinonaktifkan admin di tengah alur (dua sesi simultan) | FE+BE | TC-AUTH-OTP-100, 70 |
| TC-AUTH-OTP-E2E-010 | Penanganan provider reCAPTCHA down/timeout dan retry request OTP | mock | TC-AUTH-OTP-14, 76 |
| TC-AUTH-OTP-E2E-011 | Penanganan kegagalan server 500 dan HTTP 429 IP rate limit pada halaman Input Email | mock | TC-AUTH-OTP-27, 72, 79 |
| TC-AUTH-OTP-E2E-012 | Tampilan mobile responsive halaman Input Email dan peniadaan reCAPTCHA | mock | TC-AUTH-OTP-2, 13, 98 |

### Fase 2: Eksekusi Request OTP & Konkurensi
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-013 | Request OTP sukses, proteksi double-submit, dan toast notifikasi pengiriman | FE+BE | TC-AUTH-OTP-12, 25, 30 |
| TC-AUTH-OTP-E2E-014 | Permintaan OTP baru meng-invalidate kode sebelumnya dan navigasi kembali ke Login Password | FE+BE | TC-AUTH-OTP-26, 112 |
| TC-AUTH-OTP-E2E-015 | Penanganan dua permintaan Request OTP paralel pada dua tab browser untuk email yang sama | FE+BE | TC-AUTH-OTP-78 |

### Fase 3: Halaman Input OTP (Screening, Aksesibilitas, Mobile, Mekanisme Input)
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-016 | Screening elemen halaman Input OTP (judul, unmasked email subtitle, 6 box, autofocus, tanpa tombol Verify) | FE+BE | TC-AUTH-OTP-31, 36, 37 |
| TC-AUTH-OTP-E2E-017 | Aksesibilitas keyboard, navigasi urutan fokus Tab, dan atribut aria-label pada 6 digit OTP | FE+BE | TC-AUTH-OTP-94 |
| TC-AUTH-OTP-E2E-018 | Tampilan mobile responsive halaman Input OTP, numeric keyboard inputmode, dan tap target >= 44px | mock | TC-AUTH-OTP-32, 99 |
| TC-AUTH-OTP-E2E-019 | Mekanisme pengetikan digit OTP, backward deletion, auto-advance, dan blokir non-angka | FE+BE | TC-AUTH-OTP-33, 34, 35 |
| TC-AUTH-OTP-E2E-020 | Mekanisme auto-paste pada field OTP (paste 6 digit, truncation >6 karakter, dan sanitasi non-angka) | FE+BE | TC-AUTH-OTP-109, 110, 111 |

### Fase 4: Verifikasi OTP & Penanganan Kegagalan
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-021 | Verifikasi OTP gagal karena kode salah, clearing field, dan reset fokus | FE+BE | TC-AUTH-OTP-40, 47, 69 |
| TC-AUTH-OTP-E2E-022 | Verifikasi OTP gagal karena kode kedaluwarsa setelah melewati masa berlaku 5 menit | FE+BE | TC-AUTH-OTP-41, 69 |
| TC-AUTH-OTP-E2E-023 | Kode OTP hanya dapat digunakan satu kali dan ditolak saat disubmit ulang | FE+BE | TC-AUTH-OTP-44, 69 |
| TC-AUTH-OTP-E2E-024 | Kegagalan verifikasi OTP berulang tidak memengaruhi lock progression pada Login Password | FE+BE | TC-AUTH-OTP-45, 102 |
| TC-AUTH-OTP-E2E-025 | Akun yang sedang mengalami lock aktif di jalur Password tetap dapat login sukses via OTP | FE+BE | TC-AUTH-OTP-103 |
| TC-AUTH-OTP-E2E-026 | Penanganan kegagalan server saat verifikasi OTP, tombol fallback Verify, dan validasi field kosong | mock | TC-AUTH-OTP-43, 46, 72, 83 |

### Fase 5: Alur Resend OTP
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-027 | Alur Resend OTP dengan cooldown 1 menit dan timer aksesibilitas | FE+BE | TC-AUTH-OTP-48, 49, 96 |
| TC-AUTH-OTP-E2E-028 | Pengiriman ulang OTP sukses (resend 1-4), persistensi countdown pasca refresh F5, dan zero audit log | FE+BE | TC-AUTH-OTP-50, 55, 56 |
| TC-AUTH-OTP-E2E-029 | Batas kuota resend ke-5 memicu cooldown 10 menit dan status exhausted permanen | FE+BE | TC-AUTH-OTP-52, 53, 56 |
| TC-AUTH-OTP-E2E-030 | Penanganan kegagalan server 500 saat Resend OTP tanpa pengurangan kuota resend | mock | TC-AUTH-OTP-51, 72 |

### Fase 6: Alur Edit Email
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-031 | Ubah email dari halaman OTP, prefill email, dan reset sesi resend pada email sama | FE+BE | TC-AUTH-OTP-4, 58, 59 |
| TC-AUTH-OTP-E2E-032 | Penggantian ke alamat email berbeda dan penolakan kode OTP lama ("OTP invalid — email changed") | FE+BE | TC-AUTH-OTP-42, 60, 61 |

### Fase 7: Kondisi Balapan (Race Conditions)
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-033 | Penanganan balapan auto-submit ganda pada re-render cepat dan timeout client | FE+BE | TC-AUTH-OTP-75, 77 |
| TC-AUTH-OTP-E2E-034 | Penanganan balapan lintas aksi: Verify OTP auto-submit vs Resend OTP secara simultan | FE+BE | TC-AUTH-OTP-106 |
| TC-AUTH-OTP-E2E-035 | Penanganan balapan lintas aksi: Verify OTP auto-submit vs Edit Email secara simultan | FE+BE | TC-AUTH-OTP-107 |

### Fase 8: Post-Verification Gates, MFA, Plan Gating & Happy Path
| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AUTH-OTP-E2E-036 | Layar Agreement "Confirm to Continue" pasca verifikasi OTP, validasi uncheck, dan submit persetujuan | FE+BE | TC-AUTH-OTP-15, 19, 20, 108 |
| TC-AUTH-OTP-E2E-037 | Pembatalan sesi login pada layar Agreement (tutup tab / navigasi keluar) dan pencatatan audit log "Consent not given" | FE+BE | TC-AUTH-OTP-21 |
| TC-AUTH-OTP-E2E-038 | Pemicu layar Agreement pasca OTP: user idle >=30 hari dan pembaruan versi Privacy Policy | FE+BE | TC-AUTH-OTP-16, 17 |
| TC-AUTH-OTP-E2E-039 | Peniadaan (skip) layar Agreement untuk user rutin dan pengakuan shared consent lintas Login Password ke Login OTP | FE+BE | TC-AUTH-OTP-18, 22 |
| TC-AUTH-OTP-E2E-040 | Handoff ke MFA Authenticator setelah verifikasi OTP sukses pada user login pertama | FE+BE | TC-AUTH-OTP-39, 63, 66 |
| TC-AUTH-OTP-E2E-041 | Handoff ke MFA Authenticator setelah verifikasi OTP sukses pada user idle >= 30 hari | FE+BE | TC-AUTH-OTP-64, 66 |
| TC-AUTH-OTP-E2E-042 | Deteksi login tak biasa memicu handoff MFA dan pengiriman email alert keamanan | FE+BE | TC-AUTH-OTP-65, 66 |
| TC-AUTH-OTP-E2E-043 | Login sukses via OTP menyerahkan evaluasi batas sesi konkuren ke Session Management | mock | TC-AUTH-OTP-104 |
| TC-AUTH-OTP-E2E-044 | Fitur Login with OTP tersedia identik di seluruh tier lisensi plan tanpa batasan | FE+BE | TC-AUTH-OTP-105 |
| TC-AUTH-OTP-E2E-045 | Login OTP happy path sukses, pembuatan sesi aktif, dan pencatatan identik di 2 surface log | FE+BE | TC-AUTH-OTP-38, 62, 68, 74, 113 |

---

## 2. Alasan TC Hanya-BE (Tidak Masuk Spec E2E)

6 TC tidak masuk ke dalam suite E2E karena menguji kontrak internal backend, inspeksi kolom database langsung, atau proteksi API murni tanpa keterlibatan antarmuka pengguna:

| TC ID | Skenario | Alasan Tidak Masuk Spec E2E |
|---|---|---|
| TC-AUTH-OTP-28 | Kode disimpan sebagai hash, bukan plaintext | Memerlukan inspeksi kolom `code_hash` langsung pada tabel database; tidak terjangkau antarmuka UI. |
| TC-AUTH-OTP-29 | Kode OTP tidak pernah dikembalikan di response/log server | Verifikasi payload mentah response REST API `POST /auth/otp/request` dan server log; wilayah uji kontrak backend. |
| TC-AUTH-OTP-73 | Penulisan log gagal → rollback keputusan auth | Menguji transaksi database atomik (DB failure injection) dan rollback sesi; tidak dapat dipicu secara realistis via UI browser. |
| TC-AUTH-OTP-80 | Kode OTP tidak pernah muncul di response verify atau log server | Verifikasi payload mentah `POST /auth/otp/verify` dan log server; wilayah uji kontrak backend. |
| TC-AUTH-OTP-81 | Validasi tetap dijalankan server meski FE dimanipulasi | Bypassing validasi frontend dengan menembak langsung payload API yang dimanipulasi; dicakup dalam suite backend API test. |
| TC-AUTH-OTP-82 | Kode OTP tidak diterima untuk email yang tidak match sesi | Pengujian parameter tampering lintas sesi langsung pada endpoint API; dicakup dalam suite backend API test. |

---

## 3. Lapisan per TC (Seluruh 101 TC Granular)

| TC ID | Skenario | Prioritas | Lapisan | Spec E2E | Mode | Catatan |
|---|---|:---:|:---:|---|:---:|---|
| TC-AUTH-OTP-1 | Buka halaman Input Email (Web) — default | P0 | E2E | TC-AUTH-OTP-E2E-001 | FE+BE | |
| TC-AUTH-OTP-2 | Buka halaman Input Email (Mobile app) — default | P0 | E2E | TC-AUTH-OTP-E2E-012 | mock | reCAPTCHA tidak tampil di mobile |
| TC-AUTH-OTP-3 | Email prefilled dari Login Password | P1 | E2E | TC-AUTH-OTP-E2E-002 | FE+BE | |
| TC-AUTH-OTP-4 | Email prefilled dari "Edit email" (kembali dari halaman OTP) | P1 | E2E | TC-AUTH-OTP-E2E-031 | FE+BE | |
| TC-AUTH-OTP-5 | Email kosong | P0 | E2E | TC-AUTH-OTP-E2E-003 | FE+BE | |
| TC-AUTH-OTP-6 | Format email salah | P0 | E2E | TC-AUTH-OTP-E2E-003 | FE+BE | |
| TC-AUTH-OTP-7 | Email belum terdaftar | P0 | E2E | TC-AUTH-OTP-E2E-004 | FE+BE | |
| TC-AUTH-OTP-8 | Email tepat 120 karakter (boundary) diterima | P1 | E2E | TC-AUTH-OTP-E2E-005 | FE+BE | |
| TC-AUTH-OTP-9 | Email 121 karakter → ditolak real-time | P1 | E2E | TC-AUTH-OTP-E2E-003 | FE+BE | |
| TC-AUTH-OTP-10 | Whitespace awal/akhir di-trim sebelum lookup | P1 | E2E | TC-AUTH-OTP-E2E-003 | FE+BE | |
| TC-AUTH-OTP-11 | reCAPTCHA kosong (web) | P0 | E2E | TC-AUTH-OTP-E2E-004 | FE+BE | |
| TC-AUTH-OTP-12 | reCAPTCHA solved → lanjut evaluasi | P0 | E2E | TC-AUTH-OTP-E2E-013 | FE+BE | |
| TC-AUTH-OTP-13 | Mobile — tidak ada widget & tidak divalidasi | P0 | E2E | TC-AUTH-OTP-E2E-012 | mock | |
| TC-AUTH-OTP-14 | Provider reCAPTCHA down/timeout | P1 | E2E | TC-AUTH-OTP-E2E-010 | mock | |
| TC-AUTH-OTP-15 | OTP verify sukses + Agreement terpicu (login pertama) | P0 | E2E | TC-AUTH-OTP-E2E-036 | FE+BE | |
| TC-AUTH-OTP-16 | OTP verify sukses + Agreement terpicu (idle ≥30 hari) | P0 | E2E | TC-AUTH-OTP-E2E-038 | FE+BE | |
| TC-AUTH-OTP-17 | OTP verify sukses + Agreement terpicu (privacy policy berubah) | P0 | E2E | TC-AUTH-OTP-E2E-038 | FE+BE | |
| TC-AUTH-OTP-18 | OTP verify sukses, tidak ada kondisi Agreement terpicu → skip | P0 | E2E | TC-AUTH-OTP-E2E-039 | FE+BE | |
| TC-AUTH-OTP-19 | Klik Continue tanpa centang → ditolak (client-side) | P0 | E2E | TC-AUTH-OTP-E2E-036 | FE+BE | |
| TC-AUTH-OTP-20 | Centang + Continue → lanjut evaluasi MFA/Portal | P0 | E2E | TC-AUTH-OTP-E2E-036 | FE+BE | |
| TC-AUTH-OTP-21 | Tutup/tinggalkan layar tanpa Continue → login dibatalkan | P0 | E2E | TC-AUTH-OTP-E2E-037 | FE+BE | Consent not given |
| TC-AUTH-OTP-22 | Accept via Login Password lalu login OTP → skip accept | P1 | E2E | TC-AUTH-OTP-E2E-039 | FE+BE | Shared consent |
| TC-AUTH-OTP-23 | Akun belum aktivasi | P0 | E2E | TC-AUTH-OTP-E2E-006 | FE+BE | |
| TC-AUTH-OTP-24 | Akun inactive (Toggle Global OFF) | P0 | E2E | TC-AUTH-OTP-E2E-007 | FE+BE | |
| TC-AUTH-OTP-25 | Happy path — OTP terkirim & valid 5 menit | P0 | E2E | TC-AUTH-OTP-E2E-013 | FE+BE | |
| TC-AUTH-OTP-26 | Request baru meng-invalidate kode aktif sebelumnya | P0 | E2E | TC-AUTH-OTP-E2E-014 | FE+BE | |
| TC-AUTH-OTP-27 | Pengiriman gagal (5xx/internet) | P0 | E2E | TC-AUTH-OTP-E2E-011 | mock | |
| TC-AUTH-OTP-28 | Kode disimpan sebagai hash, bukan plaintext | P0 | BE | — | — | DB inspection |
| TC-AUTH-OTP-29 | Kode OTP tidak pernah dikembalikan di response/log | P0 | BE | — | — | Contract inspection |
| TC-AUTH-OTP-30 | Double-submit Request OTP (klik ganda) | P0 | E2E | TC-AUTH-OTP-E2E-013 | FE+BE | |
| TC-AUTH-OTP-31 | 6 field numerik, kursor di field 1, judul halaman | P0 | E2E | TC-AUTH-OTP-E2E-016 | FE+BE | |
| TC-AUTH-OTP-32 | Mobile — keyboard angka langsung muncul | P1 | E2E | TC-AUTH-OTP-E2E-018 | mock | `inputmode="numeric"` |
| TC-AUTH-OTP-33 | Ketik digit → auto-advance ke field berikutnya | P0 | E2E | TC-AUTH-OTP-E2E-019 | FE+BE | |
| TC-AUTH-OTP-34 | Backspace pada field kosong → backward deletion | P1 | E2E | TC-AUTH-OTP-E2E-019 | FE+BE | |
| TC-AUTH-OTP-35 | Karakter non-numerik ditolak di level input | P1 | E2E | TC-AUTH-OTP-E2E-019 | FE+BE | |
| TC-AUTH-OTP-36 | Button Verify TIDAK tampil pada happy path | P1 | E2E | TC-AUTH-OTP-E2E-016 | FE+BE | |
| TC-AUTH-OTP-37 | Subtitle menampilkan email tujuan penuh (tidak di-mask) | P1 | E2E | TC-AUTH-OTP-E2E-016 | FE+BE | |
| TC-AUTH-OTP-38 | Digit ke-6 benar → auto-submit → sukses tanpa MFA | P0 | E2E | TC-AUTH-OTP-E2E-045 | FE+BE | |
| TC-AUTH-OTP-39 | Digit ke-6 benar + trigger MFA | P0 | E2E | TC-AUTH-OTP-E2E-040 | FE+BE | |
| TC-AUTH-OTP-40 | Digit ke-6 salah | P0 | E2E | TC-AUTH-OTP-E2E-021 | FE+BE | |
| TC-AUTH-OTP-41 | OTP expired (>5 menit) | P0 | E2E | TC-AUTH-OTP-E2E-022 | FE+BE | |
| TC-AUTH-OTP-42 | Kode email lama dipakai setelah ganti email | P0 | E2E | TC-AUTH-OTP-E2E-032 | FE+BE | |
| TC-AUTH-OTP-43 | OTP kosong — verify via fallback button | P1 | E2E | TC-AUTH-OTP-E2E-026 | mock | |
| TC-AUTH-OTP-44 | Kode sudah dipakai (one-time use, tab ganda) | P0 | E2E | TC-AUTH-OTP-E2E-023 | FE+BE | |
| TC-AUTH-OTP-45 | Verifikasi OTP TIDAK menambah lock progression password | P0 | E2E | TC-AUTH-OTP-E2E-024 | FE+BE | |
| TC-AUTH-OTP-46 | Auto-submit gagal transport (network/5xx) | P0 | E2E | TC-AUTH-OTP-E2E-026 | mock | Fallback button Verify muncul |
| TC-AUTH-OTP-47 | Setelah error, field bisa di-clear & kursor kembali ke field 1 | P1 | E2E | TC-AUTH-OTP-E2E-021 | FE+BE | |
| TC-AUTH-OTP-48 | Resend disabled 1 menit pertama | P0 | E2E | TC-AUTH-OTP-E2E-027 | FE+BE | |
| TC-AUTH-OTP-49 | Resend aktif setelah 1 menit | P0 | E2E | TC-AUTH-OTP-E2E-027 | FE+BE | |
| TC-AUTH-OTP-50 | Resend sukses (ke-1 s/d ke-4) | P0 | E2E | TC-AUTH-OTP-E2E-028 | FE+BE | |
| TC-AUTH-OTP-51 | Resend gagal (network/5xx) | P0 | E2E | TC-AUTH-OTP-E2E-030 | mock | |
| TC-AUTH-OTP-52 | Resend ke-5 → disable 10 menit | P0 | E2E | TC-AUTH-OTP-E2E-029 | FE+BE | Countdown 09:59 |
| TC-AUTH-OTP-53 | Setelah cooldown 10 menit habis, tetap exhausted | P0 | E2E | TC-AUTH-OTP-E2E-029 | FE+BE | Pesan statis |
| TC-AUTH-OTP-55 | Counter resend tidak bisa di-bypass via refresh halaman | P0 | E2E | TC-AUTH-OTP-E2E-028 | FE+BE | |
| TC-AUTH-OTP-56 | Resend TIDAK dicatat ke surface log | P0 | E2E | TC-AUTH-OTP-E2E-028, E2E-029 | FE+BE | |
| TC-AUTH-OTP-58 | Klik "Edit email" → kembali ke Input Email, kode lama invalid | P0 | E2E | TC-AUTH-OTP-E2E-031 | FE+BE | |
| TC-AUTH-OTP-59 | Edit email memulai sesi resend baru — walau email SAMA persis | P0 | E2E | TC-AUTH-OTP-E2E-031 | FE+BE | |
| TC-AUTH-OTP-60 | Submit email baru dari halaman Edit → kode baru terkirim | P0 | E2E | TC-AUTH-OTP-E2E-032 | FE+BE | |
| TC-AUTH-OTP-61 | Kode lama (sebelum edit) dipakai setelah edit email | P1 | E2E | TC-AUTH-OTP-E2E-032 | FE+BE | |
| TC-AUTH-OTP-62 | Happy path — tanpa trigger Agreement/MFA | P0 | E2E | TC-AUTH-OTP-E2E-045 | FE+BE | |
| TC-AUTH-OTP-63 | Trigger MFA — login pertama | P0 | E2E | TC-AUTH-OTP-E2E-040 | FE+BE | Langsung Authenticator |
| TC-AUTH-OTP-64 | Trigger MFA — idle ≥30 hari | P0 | E2E | TC-AUTH-OTP-E2E-041 | FE+BE | |
| TC-AUTH-OTP-65 | Trigger MFA — login tak biasa → email alert | P0 | E2E | TC-AUTH-OTP-E2E-042 | FE+BE | |
| TC-AUTH-OTP-66 | `Login with OTP` dicatat saat login final tuntas di MFA | P1 | E2E | TC-AUTH-OTP-E2E-040, E2E-041, E2E-042 | FE+BE | 1 log total |
| TC-AUTH-OTP-67 | Klik "Use password instead" — email terbawa | P0 | E2E | TC-AUTH-OTP-E2E-002 | FE+BE | |
| TC-AUTH-OTP-68 | Login sukses tercatat di kedua surface identik | P0 | E2E | TC-AUTH-OTP-E2E-045 | FE+BE | Session & User Log |
| TC-AUTH-OTP-69 | Verifikasi gagal tercatat di kedua surface | P0 | E2E | TC-AUTH-OTP-E2E-021, E2E-022, E2E-023 | FE+BE | |
| TC-AUTH-OTP-70 | Kondisi pra-request teridentifikasi tercatat | P0 | E2E | TC-AUTH-OTP-E2E-006, E2E-007, E2E-009 | FE+BE | Log Failed |
| TC-AUTH-OTP-71 | Kondisi tak teridentifikasi TIDAK dicatat | P0 | E2E | TC-AUTH-OTP-E2E-003, E2E-004, E2E-008 | FE+BE | |
| TC-AUTH-OTP-72 | Resend / Request-fail-transport / Login-fail TIDAK dicatat | P0 | E2E | TC-AUTH-OTP-E2E-011, E2E-026, E2E-030 | mock | |
| TC-AUTH-OTP-73 | Penulisan log gagal → rollback keputusan auth | P0 | BE | — | — | DB transaction rollback |
| TC-AUTH-OTP-74 | IP Address tercatat pada entri log | P1 | E2E | TC-AUTH-OTP-E2E-045 | FE+BE | |
| TC-AUTH-OTP-75 | Race auto-submit ganda | P0 | E2E | TC-AUTH-OTP-E2E-033 | FE+BE | |
| TC-AUTH-OTP-76 | Retry Request OTP setelah network timeout | P0 | E2E | TC-AUTH-OTP-E2E-010 | mock | |
| TC-AUTH-OTP-77 | Retry Verify OTP setelah network timeout | P0 | E2E | TC-AUTH-OTP-E2E-033 | FE+BE | |
| TC-AUTH-OTP-78 | Dua request OTP paralel (2 tab) | P1 | E2E | TC-AUTH-OTP-E2E-015 | FE+BE | |
| TC-AUTH-OTP-79 | IP rate limit terlampaui (HTTP 429) | P1 | E2E | TC-AUTH-OTP-E2E-011 | mock | |
| TC-AUTH-OTP-80 | Kode OTP tidak pernah muncul di response verify atau log server | P0 | BE | — | — | Contract inspection |
| TC-AUTH-OTP-81 | Validasi tetap dijalankan server meski FE dimanipulasi | P0 | BE | — | — | Direct API bypass |
| TC-AUTH-OTP-82 | Kode OTP tidak diterima untuk email yang tidak match sesi | P0 | BE | — | — | Parameter tampering |
| TC-AUTH-OTP-83 | FE tidak menyimpulkan sukses tanpa konfirmasi server | P1 | E2E | TC-AUTH-OTP-E2E-026 | mock | |
| TC-AUTH-OTP-94 | OTP fields dapat diakses keyboard (Tab & aria-label) | P1 | E2E | TC-AUTH-OTP-E2E-017 | FE+BE | |
| TC-AUTH-OTP-95 | Caption error terasosiasi via `aria-describedby` | P1 | E2E | TC-AUTH-OTP-E2E-003 | FE+BE | |
| TC-AUTH-OTP-96 | Resend countdown diumumkan via `role="timer"`/`aria-live` | P1 | E2E | TC-AUTH-OTP-E2E-027 | FE+BE | |
| TC-AUTH-OTP-97 | `inputmode` sesuai per field (`inputmode="email"`) | P2 | E2E | TC-AUTH-OTP-E2E-001 | FE+BE | |
| TC-AUTH-OTP-98 | Layout mobile full-screen vertical | P2 | E2E | TC-AUTH-OTP-E2E-012 | mock | |
| TC-AUTH-OTP-99 | Tap target ≥44px untuk elemen interaktif | P2 | E2E | TC-AUTH-OTP-E2E-018 | mock | |
| TC-AUTH-OTP-100 | User di-deactivate mid-flow → request diblok | P0 | E2E | TC-AUTH-OTP-E2E-009 | FE+BE | |
| TC-AUTH-OTP-101 | User dihapus → dianggap "not registered" | P1 | E2E | TC-AUTH-OTP-E2E-008 | FE+BE | Anti-enumeration |
| TC-AUTH-OTP-102 | Kegagalan verifikasi OTP TIDAK memengaruhi lock progression Password | P0 | E2E | TC-AUTH-OTP-E2E-024 | FE+BE | |
| TC-AUTH-OTP-103 | Lock aktif di Login Password TIDAK memblok Login OTP | P0 | E2E | TC-AUTH-OTP-E2E-025 | FE+BE | |
| TC-AUTH-OTP-104 | Login sukses via OTP memicu evaluasi Session Management | P2 | E2E | TC-AUTH-OTP-E2E-043 | mock | 1 web + 1 mobile |
| TC-AUTH-OTP-105 | Fitur tersedia identik lintas semua plan & entitas | P1 | E2E | TC-AUTH-OTP-E2E-044 | FE+BE | |
| TC-AUTH-OTP-106 | Cross-action race — Verify OTP (auto-submit) vs Resend OTP | P0 | E2E | TC-AUTH-OTP-E2E-034 | FE+BE | P8-8b-1 |
| TC-AUTH-OTP-107 | Cross-action race — Verify OTP vs Edit Email | P0 | E2E | TC-AUTH-OTP-E2E-035 | FE+BE | P8-8b-1 |
| TC-AUTH-OTP-108 | Screening layar "Confirm to Continue" | P1 | E2E | TC-AUTH-OTP-E2E-036 | FE+BE | |
| TC-AUTH-OTP-109 | Auto-paste tepat 6 digit valid → distribusi + auto-submit | P0 | E2E | TC-AUTH-OTP-E2E-020 | FE+BE | |
| TC-AUTH-OTP-110 | Auto-paste >6 karakter → truncate 6 digit pertama | P1 | E2E | TC-AUTH-OTP-E2E-020 | FE+BE | |
| TC-AUTH-OTP-111 | Auto-paste string dengan non-angka terselip → bersihkan | P1 | E2E | TC-AUTH-OTP-E2E-020 | FE+BE | |
| TC-AUTH-OTP-112 | Klik "Back to Login with Password" dari halaman Input OTP | P0 | E2E | TC-AUTH-OTP-E2E-014 | FE+BE | |
| TC-AUTH-OTP-113 | Device / Browser tercatat format `[Browser] on [OS]` | P1 | E2E | TC-AUTH-OTP-E2E-045 | FE+BE | GAP-178 |
