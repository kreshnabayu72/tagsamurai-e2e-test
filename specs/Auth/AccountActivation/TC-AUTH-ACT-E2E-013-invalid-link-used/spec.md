---
id: TC-AUTH-ACT-E2E-013-invalid-link-used
title: "Halaman Invalid Link Varian Used untuk Token yang Sudah Dipakai"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-83
  - TC-AUTH-ACT-84
  - TC-AUTH-ACT-127
coverage:
  web: automated
---

# Halaman Invalid Link Varian Used untuk Token yang Sudah Dipakai

## Prerequisites

- Akun aktor seeding: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Tanpa login: semua TC berjalan di halaman publik tanpa sesi aktif di browser.
- Tidak ada password atau token di spec atau fixture; password aktivasi saat seeding diambil dari `Spectra.env.ACT_PASSWORD`.
- Hook `before` (seeding API) membuat dan mengaktifkan sendiri user berikut dengan suffix per run `+{runId}-013`, menyimpan link aktivasinya (token Consumed), lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian). Spec ini tidak bergantung pada aktivasi di TC atau spec lain:
  - TC-AUTH-ACT-83 dan TC-AUTH-ACT-84: `Wahyu Maharani` (`wahyumaharani+{runId}-013@qwertysystem.net`), Activated, token Consumed
  - TC-AUTH-ACT-127: `Ilham Wibowo` (`ilhamwibowo+{runId}-013@qwertysystem.net`), Activated, token Consumed
- Kemampuan teknis: membuka tab baru.

## Test Steps

### TC-AUTH-ACT-83: Link yang sudah dipakai menampilkan halaman Invalid Link varian Used

1. Buka kembali link aktivasi user `Wahyu Maharani` yang sudah dipakai
2. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Used tampil: Title "Link Already Used", Body "This activation link has already been used. Your account has been activated.", CTA "Go to Login"
3. Verifikasi Form Set Password tidak ditampilkan
4. Verifikasi Title dan Body berbeda dari varian Expired (varian Used hanya untuk token Consumed)

### TC-AUTH-ACT-84: Klik Go to Login pada halaman Invalid Link varian Used menuju Login with Password

5. Buka kembali link aktivasi user `Wahyu Maharani` yang sudah dipakai → varian Used tampil
6. Klik CTA "Go to Login"
7. Verifikasi halaman Login with Password tampil

### TC-AUTH-ACT-127: Setelah diarahkan ke halaman Invalid Link, link yang sama tidak dapat dipakai lagi

8. Buka link aktivasi user `Ilham Wibowo` (token sudah Consumed)
9. Coba buka link tersebut sekali lagi di tab baru
10. Verifikasi `Auth > Account Activation > Invalid Link` varian Used tampil pada kedua pembukaan; form Set Password tidak ditampilkan

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Blokir karena kondisi data (prinsip 12): token sudah consumed.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
