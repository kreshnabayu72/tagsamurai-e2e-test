---
id: TC-GS-DIV-E2E-029-konflik-edit-dua-admin-last-write-wins
title: "Konflik Edit Dua Admin: Last-Write-Wins dan Field Berbeda"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-271
  - TC-GS-DIV-301
coverage:
  web: automated
---

# Konflik Edit Dua Admin: Last-Write-Wins dan Field Berbeda

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (admin kedua): Total Control (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Tabel Pre-setup TC Division tidak mencantumkan akun ini; disediakan tim FE (cara yang sama dengan suite Brand).
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var) dan berada di Global Settings > User > Division. Hook `after` menutup konteks Sesi B dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (seeding Division lewat API di hook `before`; milik spec ini, pengganti `Strategy and Planning` dan `Planning Unit` pada TC sumber; tidak menumpang spec lain):
  - `Strategy and Planning {runId}-029` dengan Code `E29A` (TC-GS-DIV-271). Nama hasil: `Strategy Office {runId}-029` (Sesi B), lalu `Planning Office {runId}-029` (Sesi A, nilai akhir).
  - `Planning Unit {runId}-029` dengan Code `PLU` (TC-GS-DIV-301). Code `PLU` dan `PLU2` memakai nilai literal TC tanpa suffix per run karena asersi bergantung pada Code itu. Hasil: Code `PLU2` (Sesi B) dan Name `Planning Unit Office {runId}-029` (Sesi A).
- Cleanup di hook `after` (tidak berasumsi seeding atau rename berhasil penuh): hapus lewat API Division bernama `Strategy and Planning {runId}-029`, `Strategy Office {runId}-029`, `Planning Office {runId}-029`, `Planning Unit {runId}-029`, dan `Planning Unit Office {runId}-029` bila masih ada. Hook `before` juga menghapus lewat API sisa Division ber-Name bersuffix `-029` dari run sebelumnya (tidak berdasarkan Code saja), supaya Code `E29A`, `PLU`, dan `PLU2` tidak bentrok. Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; langkah ditandai `[Sesi A]` dan `[Sesi B]`; membaca Modal Changelog (kolom Division Name, Field, Old Value, New Value).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-DIV-271: Dua admin mengedit Name Division yang sama: Save terakhir menimpa tanpa dialog konflik

1. [Sesi A] Ketik Search `Strategy and Planning {runId}-029`, tekan Enter
2. [Sesi A] Buka row action baris `Strategy and Planning {runId}-029` lalu klik `Edit`
3. [Sesi B] Ketik Search `Strategy and Planning {runId}-029`, tekan Enter
4. [Sesi B] Buka row action baris `Strategy and Planning {runId}-029` lalu klik `Edit`
5. [Sesi B] Ubah Division Name menjadi `Strategy Office {runId}-029`
6. [Sesi B] Klik `[Save]`
7. [Sesi B] Verifikasi toast sukses: `Success, division has been updated.`
8. [Sesi A] Ubah Division Name menjadi `Planning Office {runId}-029`
9. [Sesi A] Klik `[Save]`
10. [Sesi A] Verifikasi toast sukses: `Success, division has been updated.`
11. [Sesi A] Verifikasi tidak ada dialog konflik
12. [Sesi A] Ganti isi kotak search dengan `Planning Office {runId}-029`, tekan Enter
13. [Sesi A] Verifikasi nama akhir `Planning Office {runId}-029` ada di tabel (Save terakhir menang)
14. [Sesi A] Buka Modal Changelog
15. [Sesi A] Verifikasi Changelog mencatat entri Edit Name dari `Strategy and Planning {runId}-029` ke `Strategy Office {runId}-029`
16. [Sesi A] Verifikasi Changelog mencatat entri Edit Name terpisah dari `Strategy Office {runId}-029` ke `Planning Office {runId}-029`
17. [Sesi A] Tutup Modal Changelog

### TC-GS-DIV-301: Dua admin mengedit field berbeda (Name dan Code) pada Division yang sama: tidak saling menimpa

18. [Sesi A] Ganti isi kotak search dengan `Planning Unit {runId}-029`, tekan Enter
19. [Sesi A] Buka row action baris `Planning Unit {runId}-029` lalu klik `Edit`
20. [Sesi B] Ganti isi kotak search dengan `Planning Unit {runId}-029`, tekan Enter
21. [Sesi B] Buka row action baris `Planning Unit {runId}-029` lalu klik `Edit`
22. [Sesi B] Ubah Code menjadi `PLU2`
23. [Sesi B] Klik `[Save]`
24. [Sesi B] Verifikasi toast sukses: `Success, division has been updated.`
25. [Sesi A] Ubah Division Name menjadi `Planning Unit Office {runId}-029` (Code tidak diubah)
26. [Sesi A] Klik `[Save]`
27. [Sesi A] Verifikasi toast sukses: `Success, division has been updated.`
28. [Sesi A] Verifikasi tidak ada dialog konflik
29. [Sesi A] Ganti isi kotak search dengan `Planning Unit Office {runId}-029`, tekan Enter
30. [Sesi A] Verifikasi nilai akhir Name `Planning Unit Office {runId}-029`
31. [Sesi A] Verifikasi nilai akhir Code `PLU2` (Save Sesi A tidak mengembalikan Code lama)
32. [Sesi A] Buka Modal Changelog
33. [Sesi A] Verifikasi Changelog mencatat entri Edit untuk Division `Planning Unit {runId}-029` dengan Field `Code`, Old Value `PLU`, dan New Value `PLU2`
34. [Sesi A] Verifikasi Changelog mencatat entri Edit terpisah dengan Field `Division Name`, Old Value `Planning Unit {runId}-029`, dan New Value `Planning Unit Office {runId}-029`
35. [Sesi A] Tutup Modal Changelog

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-271 dan TC-GS-DIV-301). Mode: FE+BE. Kelas harness: multi-konteks (dua admin, bagian 3 prinsip 13c).
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC: TC-GS-DIV-271 lebih dulu, lalu TC-GS-DIV-301; keduanya memakai Division milik spec sendiri dan tidak saling bergantung.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 3, 12, 18, 20, dan 29 (mencari target Edit atau baris hasil lewat Search; Search diganti nilai baru pada pencarian berikutnya); langkah 14 dan 17 serta 32 dan 35 (membuka dan menutup Modal Changelog).
- Pada kedua TC, Sesi A membuka form Edit lebih dulu (state lama tetap di form Sesi A), sehingga Sesi A menyimpan nilai dari kondisi sebelum Save Sesi B; inilah yang diuji. Asersi toast Sesi B (langkah 7 dan 24) dilakukan sebelum Sesi A bertindak (asersi state sementara tepat waktu).
- Entri Changelog pada langkah 15, 16, dan 34 unik per run karena Old Value dan New Value mengandung `{runId}-029`. Entri pada langkah 33 (Old Value `PLU`, New Value `PLU2` identik tiap run) dibedakan lewat kolom Division Name `Planning Unit {runId}-029` (nama Division saat Save Sesi B). Dengan nilai pembeda itu pencarian entri tidak memerlukan baseline waktu.
- Sesi B memakai sesi UI karena toast Sesi B diasersi (langkah 7 dan 24).
- Temuan untuk QA:
  - TC-GS-DIV-271 dan TC-GS-DIV-301 tidak menyebut Code awal `Strategy and Planning` (`SNP` pada Tabel TC) maupun apakah form Sesi A diperbarui realtime oleh Save Sesi B; spec memakai Code seeding `E29A` dan tidak mengasersi isi form Sesi A sebelum Save.
  - TC-GS-DIV-301 butir d ("dua entri Edit terpisah") tidak menyebut urutan entri di Changelog; spec mengasersi keberadaan kedua entri tanpa urutan.
  - Post Condition TC-GS-DIV-271 dan TC-GS-DIV-301 ("Name akhir ...", "Code akhir ...") memiliki padanan di Expected c.
