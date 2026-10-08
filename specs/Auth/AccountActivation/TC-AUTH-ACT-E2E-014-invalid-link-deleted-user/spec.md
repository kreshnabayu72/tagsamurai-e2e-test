---
id: TC-AUTH-ACT-E2E-014-invalid-link-deleted-user
title: "Link Aktivasi Milik User yang Dihapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-88
  - TC-AUTH-ACT-125
coverage:
  web: automated
---

# Link Aktivasi Milik User yang Dihapus

## Prerequisites

- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Password user uji dari `Spectra.env.ACT_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-014` beserta link aktivasinya; hook `after` menghapus sisa user yang masih ada (tetap jalan walau seeding gagal sebagian):
  - TC-AUTH-ACT-88: `Budi Wijaya` (`budiwijaya+{runId}-014@qwertysystem.net`), Pending Activation, token Active, lalu dihapus lewat API admin Global Settings sebelum link dibuka
  - TC-AUTH-ACT-125: `Surya Saputra` (`suryasaputra+{runId}-014@qwertysystem.net`), Pending Activation, token Active
- Kemampuan teknis: dua konteks browser (jendela privat publik dan browser admin).

## Test Steps

### TC-AUTH-ACT-88: Link milik user yang dihapus menampilkan halaman Invalid Link varian Expired

1. Di jendela privat (tanpa sesi), buka link aktivasi user `Budi Wijaya`
2. Verifikasi Halaman `Auth > Account Activation > Invalid Link` varian Expired tampil: Title "Activation Link Expired", Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
3. Verifikasi Tidak ada button CTA (tidak ada "Go to Login") pada halaman dan form Set Password tidak ditampilkan
4. Verifikasi Tampilan identik dengan link expired (tidak dibedakan dari penyebab lain)

### TC-AUTH-ACT-125: User dihapus saat form terbuka: submit diarahkan ke halaman Invalid Link

5. Di jendela privat, buka link aktivasi user `Surya Saputra` → halaman `Auth > Account Activation > Set Password` tampil
6. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
7. Ganti konteks ke browser admin: login sebagai akun aktor Total Control (Global Settings), lalu hapus user `Surya Saputra` dari `Global Settings > User > Login User`
8. Ganti konteks kembali ke jendela privat (tab form) dan klik button "Set Password"
9. Verifikasi Tab form diarahkan ke `Auth > Account Activation > Invalid Link` varian Expired (Title "Activation Link Expired")
10. Verifikasi Tidak ada akun yang teraktivasi; tidak ada toast
11. Verifikasi User `Surya Saputra` terhapus

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Blokir karena kondisi data (prinsip 12): user target dihapus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengecualian prinsip 13 (kelas c): TC-AUTH-ACT-125 (race saat admin menghapus user ketika form terbuka) tetap digabung dengan TC-AUTH-ACT-88 karena keduanya menguji user yang dihapus pada halaman yang sama; urutan publik dulu lalu browser admin, supaya ganti konteks minimal (alasan sama dengan spec 011).
