---
id: TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box
title: "Screening Halaman Activate TAG (RFID dan GPS), Info Box Device Communication Address, dan Urutan Tabel Staging"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-43
  - TC-GS-TAG-44
  - TC-GS-TAG-45
  - TC-GS-TAG-46
  - TC-GS-TAG-47
  - TC-GS-TAG-48
  - TC-GS-TAG-166
coverage:
  web: automated
---

# Screening Halaman Activate TAG (RFID dan GPS), Info Box Device Communication Address, dan Urutan Tabel Staging

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun (tiga akun; akun pertama di hook `before`, ganti akun eksplisit di langkah 41 dan 45):
  - Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi), `Spectra.env.GS_TC_PASSWORD`.
  - Manage TAG (Update) `manageTagUpdate_automated_qaTeam1@qwertysystem.net` (Agus Wijaya), `Spectra.env.GS_TAG_UPDATE_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`, lihat `suite.md` bagian Kredensial).
  - Total Control Client Quota `totalControl_automated_qaQuota@qwertysystem.net` (Fitri Handayani), `Spectra.env.GS_TC_QUOTA_PASSWORD` (belum terdaftar); GPS kuota 3 dengan terpakai 2 (sisa 1) disetel fixture BE; Communication Endpoint Client Quota terisi (disediakan tim FE).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A).
- Data Client A: Seed Registri A (RFID – Object TAG terpakai 21 dari kuota 50, GPS terpakai 1 dari kuota 30). Stok resmi untuk TC-48: GPS `356938035643001` dan `356938035643003` Available, `356938035643002` Damaged/Missing (DD-S1 sampai DD-S3).
- State global yang diubah: Communication Endpoint Client A di Admin Console > Settings > Communication Endpoint (langkah 30 dan 35). Nilai awal untuk TC-44 disetel hook `before`: Domain `device.tagsamurai.test`, IP Address `203.0.113.10` (Q-3: nilai literal tidak ditetapkan TC selain Data Uji TC-44). Hook `after` memulihkan Communication Endpoint ke nilai yang dicatat di hook `before` walau spec gagal. Akun Admin Console pelaku perubahan tidak ada di Pre-setup TC: disediakan tim FE (S-13).
- Kemampuan teknis: mengubah Communication Endpoint Client A di Admin Console (disediakan tim FE); entri manual GPS (input teks dan tombol `Add`, label menunggu desain NC-11, selektor disediakan tim FE); jumlah terpakai kuota GPS Client Quota disetel fixture BE.
- Spec tidak melakukan Submit Activation; registri Client A tidak berubah.
- Suite serial (`parallel: false`); spec tidak bergantung pada hasil spec lain. Identifier TAG (EPC, IMEI, UID) tetap dan tidak dapat diberi sufiks `{runId}` (S-12), sehingga seeding bersifat idempotent: hook `before` mengembalikan data yang dipakai spec ini ke kondisi awal (Q-4).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate` menjadi true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md` bagian Hook Guided Tooltip.
- Nilai data mengacu ke `fixtures/all-tags.json` (identitas saja, dibuat tahap script); tidak ada password di fixture.

## Test Steps

### TC-GS-TAG-43: Screening halaman Activate TAG tipe RFID – Object TAG

1. Mulai sesi Activate TAG tipe `RFID – Object TAG`: klik `+ Activate TAG`, pilih `RFID – Object TAG` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
2. Verifikasi Breadcrumb `TAG > Activate TAG`
3. Verifikasi ikon `[?]` tepat di kanan Breadcrumb
4. Verifikasi judul `Activate TAG — RFID – Object TAG`
5. Verifikasi info kuota `29 of 50 RFID – Object TAG licenses remaining.`
6. Verifikasi section `Self-Purchased Template` tampil sebagai section collapsible
7. Verifikasi section `Self-Purchased Template` dalam keadaan collapsed secara default
8. Verifikasi toolbar staging `Total Scanned: 0 | Remove | Scan TAG`
9. Verifikasi kolom tabel staging `Checkbox | Device Name | SKU | Brand | Model/Type | Code | Status | Actions`
10. Verifikasi tabel staging tanpa kolom `TAG Type` dan tanpa kolom `Source`
11. Verifikasi tabel staging kosong
12. Verifikasi footer `Clear Field | Submit`
13. Kembali ke List: klik item sidebar `TAG` (staging kosong)

### TC-GS-TAG-44: Screening halaman Activate TAG tipe GPS dan Info Box

14. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
15. Verifikasi judul `Activate TAG — GPS`
16. Verifikasi Info Box `Device Communication Address` tampil read-only di bagian paling atas halaman
17. Verifikasi Info Box memuat Domain `device.tagsamurai.test` dan IP Address `203.0.113.10` sesuai Communication Endpoint
18. Verifikasi tidak ada tombol `Remove` scan-based di toolbar
19. Verifikasi toolbar staging memuat `Total Scanned: 0`
20. Verifikasi toolbar staging memuat dropzone berkas CSV/XLSX
21. Verifikasi toolbar staging memuat input entri manual IMEI dengan tombol `Add`

### TC-GS-TAG-48: Tabel staging tidak dapat disortir dan menjaga urutan pemindaian

22. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643003` lalu `356938035643001` lalu `356938035643002` berurutan
23. Verifikasi baris staging berurutan sesuai entri: `356938035643003`, `356938035643001`, `356938035643002` (baris baru di bawah)
24. Klik header kolom `Code`, lalu `Device Name`, lalu `Status`
25. Verifikasi header kolom tidak memiliki ikon sort
26. Verifikasi klik header tidak mengubah urutan baris
27. Verifikasi tabel staging memakai scroll internal dengan header tetap
28. Verifikasi tabel staging tanpa pagination
29. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

### TC-GS-TAG-45: Info Box: baris IP Address kosong tidak dirender

30. Ubah Communication Endpoint Client A di Admin Console: kosongkan IP Address, Domain tetap `device.tagsamurai.test`, hingga tersimpan (disediakan tim FE)
31. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
32. Verifikasi Info Box hanya menampilkan baris Domain
33. Verifikasi baris IP Address tidak dirender
34. Kembali ke List: klik item sidebar `TAG` (staging kosong)

### TC-GS-TAG-46: Info Box disembunyikan total saat Domain dan IP Address kosong

35. Ubah Communication Endpoint Client A di Admin Console: kosongkan Domain dan IP Address hingga tersimpan (disediakan tim FE)
36. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
37. Verifikasi judul `Activate TAG — GPS`
38. Verifikasi Info Box tidak tampil sama sekali
39. Kembali ke List: klik item sidebar `TAG` (staging kosong)
40. Pulihkan Communication Endpoint Client A ke Domain `device.tagsamurai.test` dan IP Address `203.0.113.10` hingga tersimpan (disediakan tim FE)

### TC-GS-TAG-166: Info Box tampil untuk Manage TAG (Update)

41. Ganti akun: logout, login sebagai Manage TAG (Update) Agus Wijaya (`Spectra.env.GS_TAG_UPDATE_PASSWORD`)
42. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
43. Verifikasi Info Box `Device Communication Address` tampil read-only di bagian paling atas halaman
44. Kembali ke List: klik item sidebar `TAG` (staging kosong)

### TC-GS-TAG-47: Info Box tampil terlepas dari kuota GPS tersisa (Client Quota)

45. Ganti akun: logout, login sebagai Total Control Client Quota (`Spectra.env.GS_TC_QUOTA_PASSWORD`)
46. Setel GPS Client Quota kuota 3 dengan terpakai 2 (sisa 1) lewat fixture BE (disediakan tim FE/BE)
47. Mulai sesi Activate TAG tipe `GPS`: klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, klik `Continue` pada popup `Ready to Activate a TAG`
48. Isi Template Device Name `Queclink GV300` dan Brand `Queclink`
49. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101` sehingga pool sesi habis
50. Verifikasi Info Box tetap tampil di atas halaman setelah kuota pool habis
51. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Kelas harness: fungsional (screening) dengan state global Communication Endpoint dipulihkan di hook `after`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan di atas sekitar 35 langkah: semua blok satu kelas harness (screening halaman Activate) dan berdiri sendiri; kegagalan satu blok TC tidak membuat blok lain kehilangan makna karena tiap blok membuka sesi Activate sendiri. Ganti akun eksplisit (langkah 41 dan 45) sah menurut bagian 3 (pemisah akun, kasus b); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. TC-45 dan TC-46 mengubah Communication Endpoint (state global, dipulihkan di langkah pemulihan dan hook `after`).
- Urutan: TC-43 dan TC-44 (screening) lebih dulu, TC-48 menambah baris pada sesi GPS TC-44 (screening yang sama), lalu TC-45 dan TC-46 (mengubah state global), TC-166 (Manage TAG (Update)), TC-47 (Client Quota) paling akhir karena butuh ganti client. Urutan ini berbeda dari urutan angka TC dan sengaja agar sesi GPS dipakai bersama dan state global diubah di bagian akhir.
- Langkah penghubung (tanpa `Verifikasi`): langkah mulai sesi menggabungkan TC langkah 1 sampai 3; `Kembali ke List` dengan `Leave` hanya bila staging berisi baris, dan langkah itu adalah langkah penghubung (S-03): sesi dengan baris staging dianggap dirty sehingga keluar halaman memunculkan dialog konfirmasi; definisi dirty dan teks dialog diuji di spec 036 (TC-183 sampai TC-185, TC-111 sampai TC-113) dan tidak diasersi di spec ini. langkah 30, 35, dan pemulihan endpoint menjalankan Precondition TC-45/46 serta pemulihan state; langkah isi Template dan entri IMEI di TC-47 menjalankan langkah 4 TC-47 ("Masukkan 1 IMEI valid ... hingga pool habis") dengan IMEI Needs Info diubah menjadi Self-Purchased lewat Template (pola TC-64) agar pool benar-benar terpakai.
- Rujukan silang: TC-166 (Info Box untuk Manage TAG (Update)) bukan matriks role; Role Matrix registri ada di spec 006.
- Temuan untuk QA:
  - TC-44, TC-45, TC-46, TC-47, TC-166: nilai literal `Domain` dan `IP Address` Info Box ("sesuai Communication Endpoint") dan cara mengosongkannya tidak ditetapkan TC selain Data Uji TC-44 (Q-3); spec memakai nilai Data Uji TC-44 dan menulis pengubahan endpoint sebagai kemampuan yang disediakan tim FE.
  - TC-47 Langkah 4 tidak menyebut IMEI maupun apakah Template terisi; baris Needs Info tidak mengurangi pool sedangkan Self-Purchased/Official mengurangi pool (TC-64), sehingga spec memakai `356938035643101` dengan Template terisi dan menyetel kuota Client Quota ke sisa 1 (hanya kuota GPS 3, terpakai 1 yang ditetapkan Data Uji Pre-setup TC-64; TC-41 memakai terpakai 2).
  - TC-47 Pre-setup menyebut "Communication Endpoint terisi" tanpa nilai untuk Client Quota; tidak diasersi di spec (hanya keberadaan Info Box).
