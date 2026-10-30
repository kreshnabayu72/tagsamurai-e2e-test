---
id: TC-GS-DIV-E2E-020-create-limit-master-data-count-dan-dialog-limit-reached
title: "Create Division: Master Data Count Limit dan Dialog Limit Reached"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-72
  - TC-GS-DIV-73
  - TC-GS-DIV-75
coverage:
  web: automated
---

# Create Division: Master Data Count Limit dan Dialog Limit Reached

## Prerequisites

- Mode: FE+BE (backend nyata). Spec membuat dua Division sampai jumlah Division mencapai Master Data Count Limit.
- Akun aktor: Total Control `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: 6 Division Pre-setup (Finance, Human Resources, Legal, Operations, Compliance, Treasury) sebagai latar tabel; tidak diubah spec ini.
- Data dinamis (dibuat lewat UI oleh spec ini; Name memakai suffix per run `{runId}-020`, Code memakai nilai literal TC): `Billing {runId}-020` (Code `BIL`) dan `Collections {runId}-020` (Code `COL`) berhasil dibuat; `Disputes {runId}-020` (Code `DSP`) ditolak dan tidak tersimpan (TC-GS-DIV-75).
- Kemampuan teknis (disediakan tim FE/BE; TC sumber tidak menyebut mekanisme otomasinya): mengubah Master Data Count Limit entitas Company Automation lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits dan mengembalikannya; membaca jumlah Division lewat API; membaca total Division dari tabel; seeding dan penghapusan Division lewat API.
- State global: Master Data Count Limit entitas diubah sementara. Hook `before` mencatat nilai limit awal dan hapus lewat API sisa Division run sebelumnya yang bernama memuat `-020`, lalu membaca jumlah Division N dan menetapkan Master Data Count Limit menjadi N + 2 (dua di bawah limit, precondition TC-GS-DIV-75). Hook `after` mengembalikan limit ke nilai awal dan menghapus lewat API `Billing {runId}-020`, `Collections {runId}-020`, dan `Disputes {runId}-020` bila masih ada, tanpa berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`) karena Master Data Count Limit mempengaruhi seluruh Create Division pada entitas.
- Sesudah langkah 10, jumlah Division sama dengan Master Data Count Limit (precondition TC-GS-DIV-72 dan TC-GS-DIV-73); spec tidak mengubah limit lagi di tengah.
- Hook `afterEach`: tutup dialog atau modal Create yang masih terbuka dan kembali ke layar Division (cadangan bila langkah 24 sampai 27 atau 36 tidak tercapai).
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-GS-DIV-75: Create berulang dengan Stay checked sampai limit: data terakhir berhasil, berikutnya ditolak

1. Klik `[+ Division]`
2. Centang `Stay on this form after submitting`
3. Isi Division Name `Billing {runId}-020` dan Code `BIL`
4. Klik `[Submit]`
5. Verifikasi toast sukses: `Success, division has been created.`
6. Verifikasi form tetap terbuka
7. Verifikasi Division Name kosong (form ter-reset)
8. Verifikasi Code kosong (form ter-reset)
9. Isi Division Name `Collections {runId}-020` dan Code `COL`
10. Klik `[Submit]`
11. Verifikasi toast sukses: `Success, division has been created.`
12. Verifikasi form tetap terbuka
13. Verifikasi Division Name kosong (form ter-reset)
14. Verifikasi Code kosong (form ter-reset)
15. Isi Division Name `Disputes {runId}-020` dan Code `DSP`
16. Klik `[Submit]`
17. Verifikasi Dialog `Limit Reached` (severity warning) tampil
18. Verifikasi jumlah Division lewat API sama dengan Master Data Count Limit (membuktikan `Billing {runId}-020` dan `Collections {runId}-020` tersimpan)
19. Verifikasi record `Disputes {runId}-020` tidak dibuat: tidak ada Division bernama tersebut lewat API
20. Klik `[OK]` pada Dialog `Limit Reached`
21. Verifikasi form tetap terbuka
22. Verifikasi Division Name `Disputes {runId}-020` dipertahankan
23. Verifikasi Code `DSP` dipertahankan
24. Klik `✕` untuk menutup form yang masih dirty
25. Verifikasi dialog `Unsaved Changes` tampil
26. Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
27. Klik `[Leave]` pada dialog `Unsaved Changes`
28. Catat jumlah total Division di tabel sebagai baseline

### TC-GS-DIV-72: Klik [+ Division] saat Master Data Count Limit tercapai menampilkan Dialog Limit Reached

29. Verifikasi tombol `[+ Division]` tetap Show
30. Verifikasi tombol `[+ Division]` enabled
31. Klik `[+ Division]`
32. Verifikasi Dialog `Limit Reached` (severity warning) tampil
33. Verifikasi body dialog: `You've reached the division limit for this workspace.`
34. Verifikasi dialog hanya memiliki satu tombol `[OK]`
35. Verifikasi tidak ada modal Create

### TC-GS-DIV-73: Klik OK pada Dialog Limit Reached menutup dialog

36. Klik `[OK]`
37. Verifikasi tidak ada toast
38. Verifikasi Dialog `Limit Reached` tertutup
39. Verifikasi tidak ada modal Create
40. Verifikasi tabel tidak berubah: jumlah total Division sama dengan baseline langkah 28

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 75, 72, 73 (urutan TC sumber 72, 73, 75). Alasan: sesudah TC-GS-DIV-75 jumlah Division sama dengan Master Data Count Limit, yaitu tepat precondition TC-GS-DIV-72 dan TC-GS-DIV-73, sehingga limit hanya diubah sekali di hook `before` dan tidak diubah di tengah spec. TC-GS-DIV-73 bergantung pada TC-GS-DIV-72 (kolom Dependensi TC sumber) dan tetap sesudahnya.
- Langkah 1 TC-GS-DIV-73 ("Klik `[+ Division]`") identik dengan langkah 2 TC-GS-DIV-72 dan keadaannya (dialog `Limit Reached` tampil) dipakai bersama; satu klik (langkah 31) melayani kedua TC, lalu langkah 36 adalah langkah 2 TC-GS-DIV-73.
- Langkah 2 (mencentang `Stay on this form after submitting`) adalah langkah 1 TC-GS-DIV-75. Langkah penghubung (aksi tanpa `Verifikasi`): langkah 20 (menutup Dialog `Limit Reached` TC-GS-DIV-75 dengan `[OK]`, karena TC sumber tidak menyebut cara menutupnya), langkah 24 dan 27 (menutup form dirty lewat `✕` dan `[Leave]`; langkah 25 memverifikasi dialog `Unsaved Changes` sesuai S-08, bukan Expected TC), dan langkah 28 (mencatat baseline jumlah Division untuk langkah 40).
- Langkah 18 dan 19 mengasersi record `Disputes` tidak dibuat dengan anchor positif: jumlah Division lewat API sama dengan limit membuktikan dua Division terdahulu tersimpan.
- Kelas fungsional dengan state limit sebagai pemicu (Master Data Count Limit diatur di hook `before`). Semua TC sumber spec ini dikerjakan di sini; TC race slot terakhir dan Import yang terkait Master Data Count Limit ada di spec lain.
- Spec berada di batas sekitar 35 langkah (40 langkah) karena tiga TC limit berkelas fungsional sama dengan satu akun dan satu state limit yang dibangun sekali di hook `before`; butir Expected bermajemuk dipecah per klausa (S-01). Pemecahan hanya menambah login, hook, dan pengaturan ulang limit.
- Temuan untuk QA:
  - precondition TC-GS-DIV-72, TC-GS-DIV-73, dan TC-GS-DIV-75 mengubah Master Data Count Limit lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits, tetapi TC tidak memberi akun, cara otomasi, atau jaminan tidak ada aktor lain yang menambah Division selama spec berjalan; kemampuan itu dicatat di Prerequisites sebagai disediakan tim FE/BE.
  - TC-GS-DIV-75 Expected b tidak menyebut body dan tombol Dialog `Limit Reached`; langkah 17 hanya mengasersi dialog tampil, body dan tombol diasersi pada TC-GS-DIV-72 (langkah 33 dan 34).
  - TC-GS-DIV-75 tidak menyebut cara menutup Dialog `Limit Reached` sebelum form ditutup; spec memakai `[OK]` (langkah 20) dari Expected TC-GS-DIV-72.
