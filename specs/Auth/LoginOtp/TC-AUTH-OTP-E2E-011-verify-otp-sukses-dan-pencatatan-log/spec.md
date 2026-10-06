---
id: TC-AUTH-OTP-E2E-011-verify-otp-sukses-dan-pencatatan-log
title: "Verifikasi OTP Sukses Happy Path dan Pencatatan Log di Dua Surface"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-48
  - TC-AUTH-OTP-51
  - TC-AUTH-OTP-100
  - TC-AUTH-OTP-127
  - TC-AUTH-OTP-136
  - TC-AUTH-OTP-137
coverage:
  web: automated
---

# Verifikasi OTP Sukses Happy Path dan Pencatatan Log di Dua Surface

## Prerequisites

- Belum login dan session kosong. Halaman `Auth > Login with OTP > Request OTP` terbuka di browser.
- User `Sinta Pratama` (`sintapratama@qwertysystem.net`) profil BASE (Tabel Data Uji Pre-setup #2: sudah login dalam 30 hari terakhir, device dikenal, agreement versi terbaru sudah disetujui, MFA tidak aktif).
- User `Fikri Purnama` (`fikripurnama@qwertysystem.net`) profil BASE.
- User `Doni Wijaya` (`doniwijaya@qwertysystem.net`) profil BASE.
- Mail-catcher aktif untuk membaca kode OTP 6 digit.
- Akun admin Total Control Global Settings disiapkan untuk memeriksa Activity Log Session dan User Log.

## Test Steps

### Happy path login OTP langsung ke Product Hub tanpa gate perantara

1. Buka halaman Request OTP di browser
2. Masukkan email `sintapratama@qwertysystem.net`
3. Centang reCAPTCHA dan klik [Request OTP]
4. Verifikasi toast sukses muncul dan halaman Verify OTP tampil
5. Ambil 6 digit kode OTP dari email yang masuk ke mail-catcher
6. Masukkan 6 digit kode OTP tersebut ke dalam kotak digit
7. Verifikasi auto-submit langsung memvalidasi kode ke backend
8. Verifikasi pengguna profil BASE dialihkan langsung ke Portal — Product Hub tanpa melalui layar Agreement Gate ("Confirm to Continue")
9. Verifikasi sesi login aktif terbentuk (cookie/token tersimpan) dan nama `Sinta Pratama` tampil pada profil header

### Validasi kode dalam rentang masa berlaku aktif (< 5 menit)

10. Buka kembali halaman Request OTP dalam sesi baru
11. Masukkan email `fikripurnama@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik [Request OTP]
12. Ambil kode OTP dan biarkan berlalu selama 2 menit (masih dalam batas TTL 5 menit)
13. Masukkan 6 digit kode tersebut ke kotak digit
14. Verifikasi verifikasi berhasil dan browser diarahkan ke Portal — Product Hub

### Verifikasi pencatatan log di dua surface: Activity Log dan User Log

15. Buka sesi admin Total Control Global Settings di browser/konteks terpisah
16. Buka `Global Settings > Activity Log > Session`
17. Verifikasi terdapat satu entri baru untuk login `Sinta Pratama` dengan detail:
    - Status: "Success"
    - Method / Action: "Login with OTP" (atau representasi OTP)
    - IP Address: sesuai IP klien uji
    - Timestamp: waktu login
18. Verifikasi kolom Device / Browser menampilkan string kanonikal terstruktur (contoh: "Chrome 128 / Windows 10")
19. Buka `Global Settings > User > Detail (Sinta Pratama) > tab User Log`
20. Verifikasi terdapat satu entri baru dengan Status "Success", tanggal dan IP identik
21. Verifikasi satu kali percobaan login sukses hanya menghasilkan tepat satu baris entri di Activity Log Session dan tepat satu baris entri di User Log (invarian 1:1)

## Notes

- Profil BASE adalah profil standar di mana user sudah pernah menyetujui Privacy Policy versi terbaru, login dari perangkat yang dikenal, dan tidak memiliki konfigurasi MFA aktif; sehingga alur verifikasi langsung menembus ke Product Hub.
- Setiap aktivitas login dicatat secara atomik pada dua surface audit trail internal (Activity Log Session dan User Log).
