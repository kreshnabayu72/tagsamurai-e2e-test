---
id: TC-GS-DIV-E2E-021-create-race-slot-terakhir-dua-admin
title: "Create Division: Race Slot Terakhir antara Dua Admin"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-74
  - TC-GS-DIV-274
coverage:
  web: automated
---

# Create Division: Race Slot Terakhir antara Dua Admin

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (admin kedua): Total Control (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Tabel Pre-setup TC Division tidak mencantumkan akun ini; disediakan tim FE (cara yang sama dengan suite Brand).
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var) dan berada di Global Settings > User > Division. Hook `after` menutup konteks Sesi B dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- State global yang diubah: Master Data Count Limit Division pada entitas akun uji. Hook `before` membaca jumlah Division saat ini lalu mengatur limit menjadi jumlah itu ditambah satu (tepat satu slot kosong) lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits. Hook `after` mengembalikan limit ke nilai semula, tanpa berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Data dinamis (dibuat dan dibersihkan spec ini; tidak menumpang spec lain): `Slot Filler {runId}-021` (dibuat Sesi B lewat UI pada TC-GS-DIV-74, dihapus lewat seeding API pada langkah penghubung), `Slot A {runId}-021` dan `Slot B {runId}-021` (nama uji TC-GS-DIV-274; yang menang race tersimpan), serta `Archive Unit {runId}-021` dengan Code `ARC` (diketik pada TC-GS-DIV-74 dan tidak boleh tersimpan). Code `ARC` memakai nilai literal TC karena Code tidak diberi suffix per run; hook `before` dan `after` menghapus lewat API Division berkode `ARC` serta Division bernama `Archive Unit`, `Slot Filler`, `Slot A`, dan `Slot B` bersuffix `-021` bila ada.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; klik `[Submit]` hampir bersamaan di dua sesi; seeding dan penghapusan Division lewat API; mengubah Master Data Count Limit lewat System Limits (akun Admin Console untuk ini disediakan tim FE); langkah ditandai `[Sesi A]` dan `[Sesi B]`.

## Test Steps

### TC-GS-DIV-74: Limit tercapai saat Submit menolak Create dengan Dialog Limit Reached

1. [Sesi A] Klik `[+ Division]`
2. [Sesi A] Isi Division Name `Archive Unit {runId}-021`
3. [Sesi A] Isi Code `ARC`
4. [Sesi B] Klik `[+ Division]`
5. [Sesi B] Isi Division Name `Slot Filler {runId}-021` (Code dikosongkan)
6. [Sesi B] Klik `[Submit]`
7. [Sesi B] Tunggu hingga Create selesai (toast sukses tampil dan `Slot Filler {runId}-021` ada di tabel); jumlah Division kini sama dengan Master Data Count Limit
8. [Sesi A] Klik `[Submit]`
9. [Sesi A] Verifikasi Dialog `Limit Reached` tampil
10. [Sesi A] Verifikasi body dialog: `You've reached the division limit for this workspace.`
11. [Sesi A] Klik `[OK]`
12. [Sesi A] Verifikasi modal Create tetap terbuka
13. [Sesi A] Verifikasi Division Name `Archive Unit {runId}-021` dipertahankan
14. [Sesi A] Verifikasi Code `ARC` dipertahankan
15. [Sesi B] Muat ulang halaman Division
16. [Sesi B] Ketik Search `Slot Filler {runId}-021`, tekan Enter
17. [Sesi B] Verifikasi baris `Slot Filler {runId}-021` ada di tabel
18. [Sesi B] Ganti isi kotak search dengan `Archive Unit {runId}-021`, tekan Enter
19. [Sesi B] Verifikasi record `Archive Unit {runId}-021` tidak dibuat (tidak ada baris di tabel)
20. [Sesi A] Klik `✕` di header modal Create
21. [Sesi A] Verifikasi dialog `Unsaved Changes` tampil
22. [Sesi A] Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
23. [Sesi A] Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
24. [Sesi A] Klik `[Leave]`
25. Hapus `Slot Filler {runId}-021` lewat seeding API sehingga jumlah Division kembali satu di bawah Master Data Count Limit

### TC-GS-DIV-274: Dua admin membuat Division pada slot terakhir: hanya satu yang berhasil

26. [Sesi A] Klik `[+ Division]`
27. [Sesi B] Klik `[+ Division]`
28. [Sesi A] Isi Division Name `Slot A {runId}-021`
29. [Sesi B] Isi Division Name `Slot B {runId}-021`
30. [Sesi A dan Sesi B] Klik `[Submit]` hampir bersamaan
31. Verifikasi tepat satu sesi (sesi pemenang) menampilkan toast sukses: `Success, division has been created.`
32. [Sesi yang kalah] Verifikasi Dialog `Limit Reached` tampil
33. [Sesi yang kalah] Verifikasi body dialog: `You've reached the division limit for this workspace.`
34. [Sesi yang kalah] Verifikasi tidak ada error inline `Division Name already exists`
35. [Sesi yang kalah] Klik `[OK]`
36. [Sesi yang kalah] Verifikasi modal Create tetap terbuka
37. [Sesi yang kalah] Verifikasi Division Name yang diisi sesi itu dipertahankan
38. [Sesi yang kalah] Klik `✕` di header modal Create
39. [Sesi yang kalah] Verifikasi dialog `Unsaved Changes` tampil
40. [Sesi yang kalah] Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
41. [Sesi yang kalah] Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
42. [Sesi yang kalah] Klik `[Leave]`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-74 dan TC-GS-DIV-274). Mode: FE+BE. Kelas harness: multi-konteks (13c); Master Data Count Limit sebagai pemicu state (`P-2`, alasan: race slot terakhir butuh limit satu di atas jumlah Division).
- Spec melewati sekitar 35 langkah (42) karena tiap TC memuat dua sesi, penutupan dua form dirty yang diwajibkan S-08 (`✕`, dialog `Unsaved Changes`, `[Leave]`) dan pemulihan slot terakhir; satu kelas multi-konteks (13c) yang tidak bisa dipisah tanpa menggandakan state berat, dan blok TC-GS-DIV-274 dimulai dari state pulihan langkah 25.
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC: TC-GS-DIV-74 lebih dulu, lalu TC-GS-DIV-274. TC-GS-DIV-74 menghabiskan slot terakhir, sedangkan TC-GS-DIV-274 butuh kondisi "satu di bawah limit" lagi, sehingga langkah 25 memulihkannya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menunggu Create Sesi B selesai sebelum Sesi A melanjutkan); langkah 11 dan 35 (menutup Dialog `Limit Reached` lewat `[OK]` sebelum memeriksa modal); langkah 15 (muat ulang agar tabel Sesi B menampilkan data terbaru); langkah 16 dan 18 (Search untuk mengamati hasil di tabel Sesi B); langkah 20 sampai 24 dan 38 sampai 42 (menutup form Create yang dirty lewat `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]`); langkah 25 (seeding API: memulihkan satu slot kosong).
- Pemenang race tidak deterministik, jadi langkah 31 sampai 42 memakai sebutan "sesi pemenang" dan "sesi yang kalah"; asersi diterapkan simetris pada kedua kemungkinan.
- Langkah 15 sampai 19 (anchor `Slot Filler` ada, lalu `Archive Unit` tidak ada) memenuhi Expected b TC-GS-DIV-74; baris anchor membuktikan tabel Sesi B sudah memuat Division milik pihak lain.
- Sesi B memakai sesi UI untuk TC-GS-DIV-274 karena hasilnya diasersi di sesi itu (toast, dialog, dan form). Pada blok TC-GS-DIV-74, Sesi B membuat `Slot Filler {runId}-021` dan membaca tabel lewat sesi UI yang sama karena sesi tersebut sudah ada.
- Body Dialog `Limit Reached` pada langkah 33 (langkah "sesi yang kalah") mengikuti body dialog yang sama pada TC-GS-DIV-72 dan Expected a TC-GS-DIV-74 ("Dialog yang sama"); Expected b TC-GS-DIV-274 hanya menyebut nama dialog.
- Langkah 34 menerjemahkan frasa "bukan pesan duplicate" pada Expected b TC-GS-DIV-274 menjadi asersi tidak adanya error inline `Division Name already exists`.
- Temuan untuk QA:
  - TC-GS-DIV-74 langkah 2 ("Admin lain membuat 1 Division") tidak menyebut caranya; spec memakai Sesi B lewat UI dengan Name `Slot Filler {runId}-021` dan Code kosong.
  - Entitas yang Master Data Count Limit-nya diubah dan akun Admin Console yang dipakai tidak disebut TC maupun Tabel Pre-setup; spec memakai entitas akun Total Control dan meminta tim FE menyediakan akun serta cara mengubah limit.
  - Post Condition TC-GS-DIV-74 ("Jumlah Division tidak melebihi limit") dan TC-GS-DIV-274 ("Jumlah Division = Master Data Count Limit") tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-GS-DIV-74 menulis Code `ARC` literal; spec mempertahankannya (tidak bersuffix) dan membersihkannya lewat API.
