---
id: TC-AC-PP-E2E-014-capability-dicabut-saat-aksi-berjalan
title: "Capability Update Dicabut Setelah Modal Edit Terbuka: Publish Ditolak 403"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-84
coverage:
  web: automated
---

# Capability Update Dicabut Setelah Modal Edit Terbuka: Publish Ditolak 403

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai (tidak ada password di spec atau fixture; nama env `AC_INDROLE_PASSWORD` dan `AC_TC_PASSWORD` perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; selain `AC_TC_PASSWORD`, nama itu belum terdaftar):

| TC | Peran dalam spec | Email | Env var password |
|---|---|---|---|
| TC-AC-PP-84 | Aktor Standard dengan peran individual "Manage privacy policy" Read dan Update (sekali pakai, Pre-setup 18) | `individualRoleAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_INDROLE_PASSWORD` |

- Hook `before`: membuat ulang aktor sekali pakai (Pre-setup 18) lewat Fixture BE, men-seed dataset Riwayat A (Version 3 Active, 3 baris) lewat Fixture BE, lalu login sebagai aktor peran individual (akun aktor pertama). Hook `after`: menghapus aktor sekali pakai, mengembalikan dataset ke Riwayat A, dan mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`); hook ini tetap jalan walau spec gagal di tengah.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat, membuat aktor sekali pakai, dan mencabut capability Update dari peran individual (TC-AC-PP-84 langkah 1).
- Suite berjalan serial (`parallel: false`) karena spec mengubah capability dan dokumen Privacy Policy bersifat tunggal platform-wide.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).

## Test Steps

### TC-AC-PP-84: Publish ditolak 403 karena capability Update dicabut setelah modal Edit terbuka

1. Buka Settings > Privacy Policy sebagai aktor peran individual
2. Klik `[⋯]` pada baris `Version 3`
3. Pilih `Edit`
4. Tunggu konten termuat
5. Klik di akhir konten editor
6. Ketik " Capability revoked." (konten sudah diubah)
7. Melalui Fixture BE, cabut capability Update dari peran individual aktor (menjadi Read saja)
8. Klik `[Publish New Version]`
9. Klik `[Publish]` pada Dialog Publish Confirm
10. Verifikasi muncul toast error "You don't have permission to do this."
11. Verifikasi Dialog Publish Confirm tertutup
12. Verifikasi modal tetap terbuka di state Edit
13. Verifikasi konten yang sudah diubah dipertahankan di editor
14. Klik `[✕]` pada header modal
15. Verifikasi Dialog "Unsaved Changes" tampil
16. Klik `[Leave]`
17. Verifikasi tabel menampilkan 3 baris Riwayat A dengan `Version 3` berbadge `Active`
18. Verifikasi tidak ada `Version 4`
19. Muat ulang halaman (refresh UI)
20. Klik `[⋯]` pada baris `Version 3`
21. Verifikasi opsi `Edit` tidak ada di dropdown (hanya `Detail`)
22. Pilih `Detail`
23. Tunggu konten termuat
24. Verifikasi footer Modal View tidak menampilkan tombol `[Edit]`
25. Klik `[✕]` pada header modal

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini dipisah dari TC-AC-PP-169 (spec `TC-AC-PP-E2E-059-capability-diberikan-dan-dicabut-akses-menu`) karena dua keluarga akun dan gabungan keduanya melewati batas ukuran spec (bagian 3, S-10).
- Langkah penghubung: langkah 14-16 (menutup modal Edit yang dirty lewat `✕` lalu `[Leave]`) dan langkah 25 (menutup Modal View bersih tanpa dialog).
- Penyimpangan urutan TC-AC-PP-84: Expected b (tabel tidak berubah, tanpa versi baru) diasersi setelah modal ditutup (langkah 14-18) karena tabel berada di belakang modal selama Expected c; Expected d (elemen yang tidak berhak tersembunyi setelah refresh) mengikuti sesudahnya. Tombol `[Publish New Version]` hanya ada di state Edit; ketiadaannya setelah refresh dibuktikan lewat ketiadaan jalur masuk ke state Edit (`Edit` pada dropdown dan `[Edit]` pada footer Modal View, langkah 21 dan 24).
- Temuan untuk QA: (1) TC-AC-PP-84 Precondition c menyebut "konten sudah diubah" tanpa teks; spec memakai teks " Capability revoked." sebagai nilai uji. (2) TC-AC-PP-84 Expected d menyebut `Publish New Version` tersembunyi setelah refresh, padahal tombol itu hanya ada di state Edit. (3) Post Condition TC-AC-PP-84 tidak punya langkah observasi di TC sehingga tidak diasersi (aktor sekali pakai dibuat ulang per TC lewat hook).
