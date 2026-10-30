---
id: TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename
title: "Edit Division Sukses: Code Uppercase, Hanya Code, Name dan Code, Division Seed, dan Rename"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-93
  - TC-GS-DIV-102
  - TC-GS-DIV-103
  - TC-GS-DIV-109
  - TC-GS-DIV-104
coverage:
  web: automated
---

# Edit Division Sukses: Code Uppercase, Hanya Code, Name dan Code, Division Seed, dan Rename

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var), lalu sesi dipakai sepanjang spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (seeding Division lewat API di hook `before`; target Edit milik spec ini, pengganti `Administration`, `Procurement`, `Production`, dan `Warehouse` pada TC sumber, serta `Seed Edit` untuk TC-GS-DIV-104; tidak menumpang spec lain atau Population D-02):
  - `Administration {runId}-027` dengan Code awal `E27A` (TC-GS-DIV-93), Code diubah menjadi ` adm-9 ` dan tersimpan `ADM-9`.
  - `Procurement {runId}-027` dengan Code awal `E27B` (TC-GS-DIV-102), Code diubah menjadi `PROC`.
  - `Production {runId}-027` dengan Code awal `E27C` (TC-GS-DIV-103), diubah menjadi `Manufacturing {runId}-027` dengan Code `MFG`.
  - `Warehouse {runId}-027` dengan Code awal `E27D` (TC-GS-DIV-109), diubah menjadi `Warehouse and Distribution {runId}-027`.
  - `Seed Edit {runId}-027` dengan Code `SED` (Data Uji Dinamis D-24, TC-GS-DIV-104), diubah menjadi `Seed Edit Renamed {runId}-027`; Code `SED` tidak berubah.
- Code hasil `ADM-9`, `PROC`, dan `MFG` serta Code awal `E27A` sampai `E27D` dan `SED` memakai nilai literal tanpa suffix per run karena asersi TC bergantung pada Code hasil uppercase dan trim. Hook `before` dan `after` menghapus lewat API Division berkode itu serta Division bersuffix `-027` bila ada.
- Cleanup di hook `after` (tidak berasumsi seeding atau rename berhasil penuh): hapus lewat API Division bernama `Administration {runId}-027`, `Procurement {runId}-027`, `Production {runId}-027`, `Manufacturing {runId}-027`, `Warehouse {runId}-027`, dan `Warehouse and Distribution {runId}-027`, `Seed Edit {runId}-027`, dan `Seed Edit Renamed {runId}-027`, serta Division berkode `E27A` sampai `E27D`, `SED`, `ADM-9`, `PROC`, dan `MFG`, bila masih ada. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: mengetik karakter huruf kecil dan spasi tepi pada Code; memuat ulang halaman (F5); seeding dan penghapusan Division lewat API.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Division Pre-setup tidak diubah spec ini; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-DIV-93: Edit Code dengan huruf kecil disimpan uppercase dan ter-trim

1. Ketik Search `Administration {runId}-027`, tekan Enter
2. Buka row action baris `Administration {runId}-027` lalu klik `Edit`
3. Ubah Code menjadi ` adm-9 ` (huruf kecil dengan spasi di awal dan akhir)
4. Verifikasi isi field Code berubah menjadi huruf besar otomatis saat mengetik
5. Klik `[Save]`
6. Verifikasi toast sukses: `Success, division has been updated.`
7. Verifikasi tabel menampilkan Code `ADM-9` tanpa spasi

### TC-GS-DIV-102: Edit hanya Code berhasil dan Name tidak berubah

8. Ganti isi kotak search dengan `Procurement {runId}-027`, tekan Enter
9. Buka row action baris `Procurement {runId}-027` lalu klik `Edit`
10. Ubah Code menjadi `PROC`
11. Klik `[Save]`
12. Verifikasi toast sukses: `Success, division has been updated.`
13. Muat ulang halaman (F5)
14. Ketik Search `Procurement {runId}-027`, tekan Enter
15. Verifikasi baris menampilkan Code `PROC`
16. Verifikasi baris menampilkan Name `Procurement {runId}-027` (tidak berubah)

### TC-GS-DIV-103: Edit Division Name dan Code sekaligus berhasil

17. Ganti isi kotak search dengan `Production {runId}-027`, tekan Enter
18. Buka row action baris `Production {runId}-027` lalu klik `Edit`
19. Ubah Division Name menjadi `Manufacturing {runId}-027`
20. Ubah Code menjadi `MFG`
21. Klik `[Save]`
22. Verifikasi toast sukses: `Success, division has been updated.`
23. Ganti isi kotak search dengan `Manufacturing {runId}-027`, tekan Enter
24. Verifikasi tabel menampilkan Name `Manufacturing {runId}-027`
25. Verifikasi tabel menampilkan Code `MFG`

### TC-GS-DIV-109: Rename Division tercermin di Division Name pada tabel setelah Save

26. Ganti isi kotak search dengan `Warehouse {runId}-027`, tekan Enter
27. Buka row action baris `Warehouse {runId}-027` lalu klik `Edit`
28. Ubah Division Name menjadi `Warehouse and Distribution {runId}-027`
29. Klik `[Save]`
30. Verifikasi toast sukses: `Success, division has been updated.`
31. Ganti isi kotak search dengan `Warehouse and Distribution {runId}-027`, tekan Enter
32. Verifikasi tabel langsung menampilkan `Warehouse and Distribution {runId}-027`

### TC-GS-DIV-104: Division hasil seeding dapat di-Edit seperti Division lain

33. Ganti isi kotak search dengan `Seed Edit {runId}-027`, tekan Enter
34. Buka row action baris `Seed Edit {runId}-027` lalu klik `Edit`
35. Verifikasi modal Edit terbuka
36. Ubah Division Name menjadi `Seed Edit Renamed {runId}-027`
37. Verifikasi Division Name dapat diubah (field berisi `Seed Edit Renamed {runId}-027`)
38. Klik `[Save]`
39. Verifikasi toast sukses: `Success, division has been updated.`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-93, 102, 103, 104, 109). Mode: FE+BE. Kelas harness: aksi sukses.
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC berbeda dari urutan nomor TC sumber: TC-GS-DIV-104 terakhir; seluruh TC memakai Division milik spec dan tidak saling bergantung.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 14, 17, 23, 26, 31, dan 33 (mencari target Edit atau baris hasil lewat Search; Search diganti nilai baru pada pencarian berikutnya). Langkah 13 (F5) adalah langkah 4 TC-GS-DIV-102.
- TC-GS-DIV-109 menyebut Post Condition "Rename tercermin ke dropdown Division pada form User dan Non-Login User (diuji di Section 7)"; observasinya tidak ada di TC ini sehingga tidak diasersi (kelas lintas modul, spec 069 dan 070).
- Temuan untuk QA:
  - TC-GS-DIV-93 butir a menyebut huruf besar otomatis saat mengetik tetapi tidak menyebut apakah spasi tepi sudah terpangkas di field; spec hanya mengasersi huruf besar di field dan hasil ter-trim di tabel.
  - Post Condition TC-GS-DIV-93 ("Code Administration menjadi ADM-9") dan TC-GS-DIV-102 ("Code Procurement menjadi PROC") memiliki padanan di Expected.
- Spec melewati sekitar 35 langkah (39 langkah) karena memuat lima TC aksi sukses yang masing-masing mengedit Division sendiri; seluruhnya satu kelas harness (aksi sukses) dan tiap blok memakai Division sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
