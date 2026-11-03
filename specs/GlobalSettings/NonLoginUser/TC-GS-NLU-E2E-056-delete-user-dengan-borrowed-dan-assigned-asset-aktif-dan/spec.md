---
id: TC-GS-NLU-E2E-056-delete-user-dengan-borrowed-dan-assigned-asset-aktif-dan
title: "Delete: User dengan Borrowed dan Assigned Asset Aktif serta Pemakaian Ulang Email dan Employee ID"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-190
  - TC-GS-NLU-193
coverage:
  web: automated
---

# Delete: User dengan Borrowed dan Assigned Asset Aktif serta Pemakaian Ulang Email dan Employee ID

## Prerequisites

- Mode: FE+BE (backend nyata). Spec menghapus satu Non-Login User bertransaksi aset dan membuat satu Non-Login User baru.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API): `Budi Kurniawan {runId}-056` (Active, Position Field Technician, Division Operations, Represented By Ahmad Fauzi) dengan dua Borrowed Asset aktif dan dua Assigned Asset aktif mengikuti pola Pre-setup No. 14 (Budi Kurniawan); Non-Login User bantuan `Pakai Ulang` (Last Name `Lama {runId}-056`) dengan Email `hapuspakaiulang+{runId}-056@qwertysystem.net` dan Employee ID `HPU-{runId}-056` yang di-seed lalu dihapus (soft-deleted) lewat API di hook `before` (precondition TC-193, dipakai sebagai precondition TC, tidak diasersi). Email dan Employee ID Pre-setup `hapuspakaiulang@qwertysystem.net` dan `HPU-001` diganti nilai bersuffix agar run berikutnya tidak bentrok (S-12).
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanismenya): seeding transaksi Borrow dan Assignment FAMS untuk user milik spec; membaca riwayat transaksi Borrow/Assignment di modul FAMS.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`). Hook `after` juga menghapus lewat API Non-Login User baru yang dibuat langkah 8 (`Pakai Ulang {runId}-056` dengan Email di atas).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-190: Delete user dengan Borrowed dan Assigned Asset aktif

1. Ketik Search `Budi Kurniawan {runId}-056`, tekan Enter
2. Klik `⋯` pada baris `Budi Kurniawan {runId}-056` > `Delete`
3. Verifikasi dialog Delete biasa tampil: Title `Delete Non-Login User`, bullet `Budi Kurniawan {runId}-056`, body `All historical records (borrowed/assigned assets) will remain, but this identity cannot be restored. This action cannot be undone. Are you sure you want to delete it?`, dan tombol `[Cancel]` dan `[Delete]`
4. Verifikasi tidak ada dialog blok dan tidak ada peringatan tambahan di dialog
5. Klik `[Delete]`
6. Verifikasi toast sukses: `Success, non-login user has been deleted.`
7. Verifikasi riwayat transaksi Borrow dan Assignment user tersebut tetap tersimpan sebagai snapshot di modul FAMS

### TC-GS-NLU-193: Email dan Employee ID user yang dihapus dapat dipakai ulang

8. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
9. Isi First Name `Pakai`, Last Name `Ulang {runId}-056`, Email `hapuspakaiulang+{runId}-056@qwertysystem.net`, Employee ID `HPU-{runId}-056`, Division `Logistics`, dan pilih Represented By `Ahmad Fauzi`
10. Klik `[Submit]`
11. Verifikasi toast sukses: `Success, non-login user has been created.`
12. Verifikasi tidak ada pesan `Email already exists`
13. Verifikasi tidak ada pesan `Employee ID already exists`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Langkah 3 dan sesudahnya: TC-190 Expected a memuat dua klausa (dialog identik; tidak ada dialog blok dan peringatan tambahan) dan ditulis sebagai dua `Verifikasi` (anchor absence: dialog Delete biasa tampil pada langkah 3).
- Langkah 11 sampai sesudahnya: toast sukses ditaruh lebih dulu sebagai anchor positif (respons server selesai) sebelum asersi absence pesan error (bagian 8b butir 2 dan 5); urutan di TC Expected adalah a (absence) lalu b (toast).
- Email dan Employee ID literal Pre-setup diganti nilai bersuffix; Last Name memuat suffix agar Name unik.
- Temuan untuk QA:
  - TC-190 Expected c (riwayat transaksi tersimpan sebagai snapshot di modul FAMS) tidak memberi langkah observasi; spec memakai kemampuan baca FAMS yang disediakan tim FE/BE.
  - TC-193 tidak menyebut Position dan nilai field wajib lain selain yang tertulis; spec mengisi persis nilai TC dan menambah suffix pada Last Name, Email, dan Employee ID.
  - Batas panjang Employee ID tidak disebut TC; nilai `HPU-{runId}-056` diasumsikan muat.
