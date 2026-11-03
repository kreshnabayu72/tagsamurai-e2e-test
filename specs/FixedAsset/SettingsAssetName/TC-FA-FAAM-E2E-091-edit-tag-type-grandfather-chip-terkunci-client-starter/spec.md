---
id: TC-FA-FAAM-E2E-091-edit-tag-type-grandfather-chip-terkunci-client-starter
title: "Edit TAG Type Grandfather: Chip Terkunci Tetap Tampil, Dapat Dilepas, dan Tidak Dapat Dipilih Lagi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-205
  - TC-FA-FAAM-206
coverage:
  web: automated
---

# Edit TAG Type Grandfather: Chip Terkunci Tetap Tampil, Dapat Dilepas, dan Tidak Dapat Dipilih Lagi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control pada Client Starter pasca-downgrade (Pre-setup #16c). Email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite, dan hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #16c: Client Starter pasca-downgrade dengan Asset Name `Grandfather Item` (Code asli tidak tertulis di TC, TAG Type `RFID` hasil grandfathering, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.grandfatherItem`. TC-205 mengubah Code `Grandfather Item` menjadi `GF2`; fixture dipulihkan ke keadaan Pre-setup #16c lewat seed reset client (disediakan tim FE/BE) di hook `before` dan `after`. Efek yang tersisa: Last Updated dan entri audit trail client itu bertambah (S-06).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-206: Chip terkunci dilepas tidak dapat dipilih lagi

1. Ketik Search `Grandfather Item`, tekan Enter
2. Klik `⋯` baris `Grandfather Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Lepas chip TAG Type `RFID`
4. Buka dropdown TAG Type dan coba pilih `RFID`
5. Verifikasi opsi `RFID` terkunci 🔒 dengan tooltip `Upgrade to unlock`
6. Verifikasi opsi `RFID` tidak dapat dipilih lagi
7. Klik `[✕]` pada modal Edit
8. Verifikasi dialog `You have unsaved changes. Are you sure you want to leave?` tampil
9. Klik `[Leave]`

### TC-FA-FAAM-205: Chip TAG Type terkunci hasil grandfathering tetap tampil dan simpan tanpa ubah diterima

10. Klik `⋯` baris `Grandfather Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
11. Verifikasi chip `RFID` tampil terkunci 🔒
12. Verifikasi chip `RFID` dapat dilepas
13. Ubah Code menjadi `GF2` tanpa mengubah chip `RFID`
14. Klik `[Save]`
15. Verifikasi toast `Success, asset name has been updated.` tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 untuk menemukan baris target (R-16); penutupan form dirty pada langkah 7 (✕, dialog Unsaved Changes, `[Leave]`, S-08).
- Urutan TC: TC-FA-FAAM-206 (tanpa simpan) lebih dulu, lalu TC-FA-FAAM-205 (simpan) (S-10). Kedua TC memakai client dan akun yang berbeda dari spec Edit lain, sehingga login akun ini dilakukan di hook `before` spec ini; spec ini dipisah dari spec 065 karena akun dan client berbeda.
- Langkah Uji TC-FA-FAAM-205 "Save sukses" diasersi lewat toast `Success, asset name has been updated.` yang sama dengan Edit sukses lain.
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-205 dan TC-FA-FAAM-206 memakai client Pre-setup #16c tetapi tabel Pre-setup tidak memuat email akun Total Control client itu dan tidak menyebut Code asli `Grandfather Item`.
  - TC-FA-FAAM-205 Expected b "Save sukses" tidak menyebut teks toast; spec memakai toast Edit sukses dari TC-FA-FAAM-183.
