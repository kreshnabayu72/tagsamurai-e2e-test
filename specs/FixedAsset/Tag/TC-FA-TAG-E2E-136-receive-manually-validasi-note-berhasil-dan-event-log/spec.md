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
- Data Pre-setup (literal TC, seeding idempotent lewat fixture backend; fixture `fixed-asset-tag.json` belum ada): Tag To Be Returned `RF-00071` (RFID, Last Asset `Excavator 20 Ton - 2`, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), `RF-00088` (RFID, `Excavator 20 Ton - 5`, Disposal Center, Dedi K.), dan `NF-00092` (NFC, `Laptop Pro 14 - 8`, HQ Warehouse, Rina T.); ini himpunan minimum, jumlah total Tag To Be Returned tidak diasersi (badge dibaca sebagai baseline N pada langkah 2).
- Kemampuan teknis (disediakan tim FE/BE): pemulihan status Tag ke To be Returned lewat fixture backend; pembacaan jumlah entri Event Log `RF-00071` sebelum aksi (baseline M pada langkah 26; audit trail permanen, M tidak dapat diturunkan dari seeding; bagian 8b butir 10).
- State global yang dipulihkan: Receive Manually menjadikan Tag Damaged/Missing di registri Global dan menambah entri Event Log To Be Returned serta TAG Log Global yang tidak dapat dihapus. Status Tag dipulihkan ke To be Returned lewat fixture backend di hook `before` dan `after` serta pada langkah 15 dan 25; entri log tetap bertambah.
- Nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik tab `To Be Returned`.
2. Catat nilai badge tab "To Be Returned" sebagai baseline N.

### TC-578: Submit tanpa Note

3. Buka menu aksi baris `RF-00071`.
4. Klik "Receive Manually".
5. Klik tombol [Submit] dengan Textarea "Note" tetap kosong.
6. Verifikasi pesan error "Note must not be empty" tampil pada field Note.
7. Verifikasi dialog tetap terbuka.
8. Verifikasi tidak ada toast sukses.

### TC-579: Receive Manually satu Tag

9. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
10. Klik tombol [Submit].
11. Verifikasi Toast "Success, TAG has been received as damaged/missing." tampil.
12. Verifikasi dialog menutup.
13. Verifikasi baris `RF-00071` hilang dari tabel.
14. Verifikasi badge tab "To Be Returned" berkurang satu terhadap baseline N dari langkah 2 (menjadi N-1).
15. Pulihkan Tag `RF-00071` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-580: Receive Manually dua Tag lewat Bulk

16. Centang baris `RF-00071` dan `RF-00088`.
17. Klik Bulk Action "Receive Manually".
18. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
19. Klik tombol [Submit].
20. Verifikasi Toast "Success, TAG has been received as damaged/missing." tampil.
21. Verifikasi dialog menutup.
22. Verifikasi baris `RF-00071` dan `RF-00088` hilang dari tabel.
23. Verifikasi Bulk Action Bar hilang.
24. Verifikasi seleksi kembali 0.
25. Pulihkan Tag `RF-00071` dan `RF-00088` ke To Be Returned lewat fixture backend, lalu muat ulang halaman dan klik tab `To Be Returned`.

### TC-581: Note tidak tampil di Event Log

26. Catat jumlah entri Event Log `RF-00071` sebelum aksi.
27. Buka menu aksi baris `RF-00071`.
28. Klik "Receive Manually".
29. Isi Textarea "Note" dengan "Tag rusak saat serah terima".
30. Klik tombol [Submit].
31. Klik "Event Log".
32. Verifikasi jumlah entri `RF-00071` bertambah satu dan entri baru memuat Method "Manual" dan Final Status "Damaged/Missing".
33. Verifikasi Modal "Event Log: To Be Returned" tidak memiliki kolom Note.
34. Verifikasi teks "Tag rusak saat serah terima" tidak muncul di modal.
35. Tutup Modal "Event Log: To Be Returned".

## Notes

- Urutan dan langkah penghubung: Dialog Receive Manually dari langkah 4 dipakai TC-578 lalu TC-579 (TC-579 mengisi Note pada dialog yang sama; Expected TC-578 sudah diasersi); langkah 1 membuka tab (hook `beforeEach` sudah membuka halaman TAG); langkah 15 dan 25 memulihkan Tag antar TC (S-09); langkah 26 mencatat baseline Event Log (S-12); langkah 35 menutup modal; langkah 2 mencatat nilai badge sebagai baseline N sebelum Dialog Receive Manually dibuka (langkah penghubung tanpa asersi, S-03) dan dipakai langkah 14 (selisih terhadap N, bukan literal 2; keputusan user 2026-11-04, bagian 8b butir 10 dan A-18 butir ii).
- Anchor absence: langkah 6 untuk langkah 8; langkah 11 untuk langkah 13; langkah 32 untuk langkah 33 dan 34. Langkah 20 menjadi anchor langkah 22.
- A-15: nilai literal Pre-setup (`RF-00071`, `RF-00088`, `NF-00092`, nama aset) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan tercatat di Prerequisites spec ini.
- Temuan untuk QA:
  - Post Condition TC-578 (tidak ada entri Event Log maupun TAG Log), TC-579 dan TC-580 (status Damaged/Missing, entri Event Log, entri TAG Log Global "Marked Damaged/Missing" dengan Previous Status dan Note) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-581 tidak menyebut baseline entri Event Log; spec memakai selisih jumlah entri `RF-00071` (S-12).
