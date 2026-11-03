---
id: TC-FA-TAG-E2E-136-receive-manually-validasi-note-berhasil-dan-event-log
title: "Receive Manually: validasi Note, berhasil satu dan dua Tag, dan Note tidak tampil di Event Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-578
  - TC-FA-TAG-579
  - TC-FA-TAG-580
  - TC-FA-TAG-581
coverage:
  web: automated
---

# Receive Manually: validasi Note, berhasil satu dan dua Tag, dan Note tidak tampil di Event Log

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.).
- Kemampuan teknis (disediakan tim FE/BE): pemulihan status Tag ke To be Returned lewat fixture backend; pembacaan jumlah entri Event Log `RF-00071` sebelum aksi (audit trail permanen, N tidak dapat diturunkan dari seeding; bagian 8b butir 10).
- State global yang dipulihkan: Receive Manually menjadikan Tag Damaged/Missing di registri Global dan menambah entri Event Log To Be Returned serta TAG Log Global yang tidak dapat dihapus. Status Tag dipulihkan ke To be Returned lewat fixture backend di hook `before` dan `after` serta pada langkah 14 dan 24; entri log tetap bertambah.

## Test Steps

1. Klik tab `To Be Returned`.

### TC-578: Submit tanpa Note

2. Buka menu aksi baris `RF-00071`.
3. Klik "Receive Manually".
4. Klik tombol [Submit] dengan Textarea "Note" tetap kosong.
5. Verifikasi pesan error "Note must not be empty" tampil pada field Note.
6. Verifikasi dialog tetap terbuka.
7. Verifikasi tidak ada toast sukses.

### TC-579: Receive Manually satu Tag

8. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
9. Klik tombol [Submit].
10. Verifikasi Toast "Success, TAG has been received as damaged/missing." tampil.
11. Verifikasi dialog menutup.
12. Verifikasi baris `RF-00071` hilang dari tabel.
13. Verifikasi badge tab "To Be Returned" menjadi 2.
14. Pulihkan Tag `RF-00071` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-580: Receive Manually dua Tag lewat Bulk

15. Centang baris `RF-00071` dan `RF-00088`.
16. Klik Bulk Action "Receive Manually".
17. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
18. Klik tombol [Submit].
19. Verifikasi Toast "Success, TAG has been received as damaged/missing." tampil.
20. Verifikasi dialog menutup.
21. Verifikasi baris `RF-00071` dan `RF-00088` hilang dari tabel.
22. Verifikasi Bulk Action Bar hilang.
23. Verifikasi seleksi kembali 0.
24. Pulihkan Tag `RF-00071` dan `RF-00088` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-581: Note tidak tampil di Event Log

25. Catat jumlah entri Event Log `RF-00071` sebelum aksi.
26. Buka menu aksi baris `RF-00071`.
27. Klik "Receive Manually".
28. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
29. Klik tombol [Submit].
30. Klik "Event Log".
31. Verifikasi jumlah entri `RF-00071` bertambah satu dan entri baru memuat Method "Manual" dan Final Status "Damaged/Missing".
32. Verifikasi Modal "Event Log: To Be Returned" tidak memiliki kolom Note.
33. Verifikasi teks "Tag rusak saat serah terima" tidak muncul di modal.
34. Tutup Modal "Event Log: To Be Returned".

## Notes

- Urutan dan langkah penghubung: Dialog Receive Manually dari langkah 3 dipakai TC-578 lalu TC-579 (TC-579 mengisi Note pada dialog yang sama; Expected TC-578 sudah diasersi); langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 14 dan 24 memulihkan Tag antar TC (S-09); langkah 25 mencatat baseline Event Log (S-12); langkah 34 menutup modal.
- Anchor absence: langkah 5 untuk langkah 7; langkah 10 untuk langkah 12; langkah 31 untuk langkah 32 dan 33. Langkah 19 menjadi anchor langkah 21.
- Temuan untuk QA:
  - Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) ditulis tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; Lampiran A konvensi belum memuat butir modul ini.
  - Post Condition TC-578 (tidak ada entri Event Log maupun TAG Log), TC-579 dan TC-580 (status Damaged/Missing, entri Event Log, entri TAG Log Global "Marked Damaged/Missing" dengan Previous Status dan Note) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-581 tidak menyebut baseline entri Event Log; spec memakai selisih jumlah entri `RF-00071` (S-12).
