---
id: TC-FA-TAG-E2E-135-receive-manually-menu-screening-dan-bulk
title: "Receive Manually: menu aksi baris, screening Dialog, dan Bulk Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-573
  - TC-FA-TAG-574
  - TC-FA-TAG-575
  - TC-FA-TAG-576
  - TC-FA-TAG-577
coverage:
  web: automated
---

# Receive Manually: menu aksi baris, screening Dialog, dan Bulk Action

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.). Spec tidak menekan [Submit], jadi status Tag tidak berubah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-573: Menu aksi baris

2. Buka menu aksi baris `RF-00071`.
3. Verifikasi menu aksi memuat satu aksi "Receive Manually" dengan ikon ArrowGoBack (severity dark).
4. Verifikasi tidak ada aksi "TAG Log" di menu.
5. Tutup menu aksi dengan tombol Esc.
6. Klik TAG Code `RF-00071`.
7. Verifikasi Popup TAG Log terbuka.
8. Tutup Popup TAG Log.

### TC-574: Screening Dialog Receive Manually dari row action

9. Buka menu aksi baris `RF-00071`.
10. Klik "Receive Manually".
11. Verifikasi Dialog "Receive Manually" (Size SM) terbuka.
12. Verifikasi ringkasan menampilkan "RF-00071 — Excavator 20 Ton - 2".
13. Verifikasi Alert info tampil dengan teks "Received TAGs leave FAMS and go back to Global Settings as Damaged/Missing. This can't be undone."
14. Verifikasi Textarea "Note" bertanda wajib (*) kosong dengan placeholder "Enter note".
15. Verifikasi footer berisi tombol [Cancel] dan [Submit].
16. Verifikasi tidak ada pilihan alasan dan tidak ada checkbox "Stay on this form after submitting".
17. Klik tombol [Cancel].

### TC-577 dan TC-576: Seleksi satu Tag dan Bulk Action

18. Centang baris `RF-00071`.
19. Verifikasi Bulk Action Bar menampilkan "1 TAG selected".
20. Verifikasi Bulk Action Bar memuat aksi "Receive Manually".
21. Klik Bulk Action "Receive Manually".
22. Verifikasi Dialog "Receive Manually" terbuka.
23. Verifikasi ringkasan menampilkan "RF-00071 — Excavator 20 Ton - 2" (bentuk satu Tag).
24. Klik tombol [Cancel].

### TC-577 dan TC-575: Seleksi dua dan tiga Tag

25. Centang baris `RF-00088`.
26. Verifikasi Bulk Action Bar menampilkan "2 TAGs selected".
27. Centang baris `NF-00092`.
28. Klik Bulk Action "Receive Manually".
29. Verifikasi Dialog "Receive Manually" terbuka.
30. Verifikasi ringkasan menampilkan "3 TAGs".
31. Verifikasi Alert info dan Textarea "Note" sama dengan dialog row action.
32. Klik tombol [Cancel].

### TC-577: Membersihkan seleksi

33. Klik ikon × pada Bulk Action Bar.
34. Verifikasi seleksi dibersihkan.
35. Verifikasi Bulk Action Bar hilang.

## Notes

- Urutan TC diubah: TC-577 dipecah menjadi tiga blok (langkah 18 sampai 20, 25 dan 26, 33 sampai 35) yang disisipi TC-576 dan TC-575, supaya seleksi bertambah satu per satu tanpa membersihkan dan memilih ulang (S-10). Isi tiap Verifikasi tetap sama dengan Expected TC.
- Langkah penghubung: langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 5 menutup menu; langkah 8, 17, 24, dan 32 menutup popup atau dialog. Langkah 3 menjadi anchor langkah 4; langkah 19 dan 20 mendahului langkah 21.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Expected b TC-573 ("TAG Log dibuka lewat klik TAG Code") tidak punya langkah di TC; spec menambahkan klik TAG Code (langkah 6) dan Verifikasi Popup TAG Log terbuka (langkah 7) sebagai langkah observasinya.
  - Expected c TC-575 ("Alert info dan Textarea Note sama dengan dialog row action") ditulis sebagai satu Verifikasi (langkah 31) sesuai butir TC.
