---
id: TC-FA-CF-E2E-159-multi-konteks-edit-bersamaan-sinkron-tabel-dan-urutan-log
title: "Multi-Konteks: Edit Bersamaan, Sinkron Tabel Antar Sesi, dan Urutan Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-598
  - TC-FA-CF-606
  - TC-FA-CF-607
  - TC-FA-CF-610
coverage:
  web: automated
---

# Multi-Konteks: Edit Bersamaan, Sinkron Tabel Antar Sesi, dan Urutan Log

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun sesi 1: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Akun sesi UI kedua (konteks browser kedua yang menjadi objek asersi, kelas c; Pre-setup #10 dan #28):

| Konteks | Company | Pre-setup | Email | Env password |
|---|---|---|---|---|
| Sesi 1 dan sesi 1b (jendela kedua akun yang sama, TC-FA-CF-606) | Company Alpha | #1 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Sesi 2 | Company Alpha | #10 | `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Rina Putri) | `Spectra.env.FA_TC2_PASSWORD` |
| Sesi 1 TC-FA-CF-607 | Company Nilai | #18 | tidak tertulis di Pre-setup TC; disediakan tim FE | `Spectra.env.FA_TC_NILAI_PASSWORD` |
| Sesi 2 TC-FA-CF-607 | Company Nilai | #18, #28 | tidak tertulis di Pre-setup TC; disediakan tim FE | `Spectra.env.FA_TC2_NILAI_PASSWORD` |

  Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12): field `Storage Capacity`, `Legacy Tag`, dan `Asset Serial Tag` (Active). Company Nilai (Pre-setup #18): `Voltage Spec` Text {Generator, Pump} Global (`Generator` = `220V`, `Pump` = `110V`). Hook `before` memulihkan baseline kedua Company (seed reset Company). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` dan `Fixture.faCustomFields.nilai` (fixture disediakan tim FE).
- Data Dinamis: Field Name hasil Edit `LWW One {runId}-159` dan `LWW Two {runId}-159`; field `Live Row {runId}-159`. Cleanup di hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-159`.
- Kemampuan teknis: dua konteks browser dengan sesi web berbeda, ditambah satu jendela kedua untuk sesi 1 (sesi 1b); kemampuan baca Modal Changelog dengan Search nama field; baseline jumlah entri dicatat sebelum aksi (S-12).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk setiap akun sesi dan hook `after` memulihkannya (lihat `suite.md`).
- State global: nama dan status field Pre-setup diubah spec ini dan nilai `Voltage Spec` diubah; hook `before` dan `after` memulihkannya lewat seed reset. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-598: dua aktor mengedit field yang sama

1. Buka konteks browser sesi 2: login sebagai Total Control sesi 2 Company Alpha dan buka Settings > Custom Fields
2. Sesi 1 dan sesi 2 membuka Edit `Storage Capacity`
3. Sesi 1 mengubah Field Name menjadi `LWW One {runId}-159` lalu klik `[Save]`
4. Verifikasi Save sesi 1 sukses tanpa dialog konflik
5. Sesi 2 mengubah Field Name menjadi `LWW Two {runId}-159` lalu klik `[Save]`
6. Verifikasi Save sesi 2 sukses tanpa dialog konflik
7. Muat ulang Settings > Custom Fields pada sesi 1
8. Verifikasi nilai akhir Field Name adalah `LWW Two {runId}-159`
9. Buka Modal Changelog, ketik Search `{runId}-159`, tekan Enter
10. Verifikasi Modal Changelog memuat dua baris Edit terpisah (satu per Save)
11. Tutup Modal Changelog

### TC-FA-CF-610: mutasi berurutan pada field yang sama oleh dua aktor

12. Catat jumlah entri Modal Changelog untuk Search `Asset Serial Tag` sebagai baseline
13. Sesi 1 menggeser switch Active baris `Asset Serial Tag` ke OFF dan klik `[Deactivate]`
14. Verifikasi toast `Success, custom field has been deactivated.` tampil pada sesi 1
15. Sesi 2 menggeser switch Active baris `Asset Serial Tag` ke ON dan klik `[Activate]` setelah sesi 1 selesai
16. Verifikasi toast `Success, custom field has been activated.` tampil pada sesi 2
17. Muat ulang Settings > Custom Fields pada sesi 1
18. Buka Modal Changelog, ketik Search `Asset Serial Tag`, tekan Enter
19. Verifikasi dua entri terbaru berurutan: Deactivate lalu Activate
20. Verifikasi jumlah entri Modal Changelog bertambah tepat dua dibanding baseline (tidak ada baris ganda)
21. Tutup Modal Changelog
22. Verifikasi switch Active baris `Asset Serial Tag` pada sesi 1 ON

### TC-FA-CF-606: tabel sesi lain menyegarkan diri dan modal Edit tidak terganggu

23. Sesi 1 ketik Search `Live Row {runId}-159`, tekan Enter
24. Verifikasi tabel sesi 1 menampilkan empty state `No results found`
25. Buka jendela kedua sesi 1 (sesi 1b): login sebagai Total Control Company Alpha, buka Settings > Custom Fields, lalu klik row action `⋯` > `Edit` pada baris `Legacy Tag` (modal Edit terbuka)
26. Sesi 2 membuat field `Live Row {runId}-159` (Data Type `Text`) lewat UI hingga tersimpan
27. Verifikasi tabel sesi 1 menambahkan baris `Live Row {runId}-159`
28. Verifikasi tabel sesi 1 menambahkan baris tanpa dialog
29. Verifikasi tabel sesi 1 tanpa reset halaman (Search `Live Row {runId}-159` tetap terisi)
30. Verifikasi modal Edit di sesi 1b tetap terbuka
31. Verifikasi input modal Edit di sesi 1b tidak berubah
32. Sesi 1b klik icon close `[✕]` pada modal Edit yang tidak diubah, lalu tutup sesi 1b
33. Sesi 1 klik `(←)` pada kotak Search

### TC-FA-CF-607: dua aktor mengubah Scope field Global bersamaan

34. Tutup sesi 2 dan `Logout` sesi 1 dari Company Alpha
35. Login sesi 1 sebagai Total Control Company Nilai dan buka Settings > Custom Fields
36. Buka konteks browser sesi 2: login sebagai Total Control sesi 2 Company Nilai dan buka Settings > Custom Fields
37. Catat jumlah entri Modal Changelog untuk Search `Voltage Spec` sebagai baseline
38. Sesi 1 dan sesi 2 membuka Edit `Voltage Spec`
39. Sesi 1 mengubah nilai `Generator` menjadi `230V` lalu klik `[Save]`
40. Verifikasi Save sesi 1 sukses tanpa dialog konflik
41. Sesi 2 mengubah nilai `Pump` menjadi `115V` lalu klik `[Save]`
42. Verifikasi Save sesi 2 sukses tanpa dialog konflik
43. Muat ulang Settings > Custom Fields pada sesi 1 dan buka Edit `Voltage Spec`
44. Verifikasi nilai akhir `Generator` = `220V` mengikuti payload penuh Save terakhir (sesi 2)
45. Verifikasi nilai akhir `Pump` = `115V`
46. Klik icon close `[✕]` pada modal Edit yang tidak diubah
47. Buka Modal Changelog, ketik Search `Voltage Spec`, tekan Enter
48. Verifikasi jumlah entri Modal Changelog bertambah tepat dua dibanding baseline (setiap Edit yang berhasil tercatat sendiri)
49. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 49 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (kelas c, dua sesi UI), berdiri sendiri, dan hasil di sesi UI kedua diasersi sehingga tidak dapat memakai sesi API; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log berpola (langkah 9 sampai 11, 18 sampai 21, 47 sampai 49) tidak dihitung (bagian 3).
- Perubahan urutan TC (S-05, S-10): TC-FA-CF-610 ditaruh sebelum TC-FA-CF-606 supaya blok Company Alpha berurutan; TC-FA-CF-607 di akhir karena memakai Company Nilai (ganti akun eksplisit di langkah 34 sampai 36).
- Sesi 1b pada TC-FA-CF-606 adalah jendela kedua akun sesi 1 untuk memegang modal Edit terbuka; sesi 2 dan sesi 1b adalah objek asersi sehingga ditulis sebagai konteks UI (bukan sesi API).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka sesi 2), langkah 7 dan 17 (memuat ulang sesi 1 supaya `Verifikasi` membaca state tersimpan), langkah 23 (Search yang menjadi anchor pembanding empty state, R-16), langkah 33 (membersihkan Search), langkah 34 sampai 36 (ganti akun), langkah 46 (menutup modal tanpa perubahan).
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Nilai dan akun sesi 2 Company Nilai; akun disediakan tim FE.
  - TC-FA-CF-598, 606, 607, dan 610 bertanda Manual Only (dua sesi paralel); TC-FA-CF-610 menyebut "Sesi 2 mengaktifkan ... setelah sesi 1 selesai" sehingga urutannya berurutan, bukan serentak.
  - TC-FA-CF-606 menyebut "sesi 1b" tanpa menyebut mekanismenya; spec memakai jendela kedua akun sesi 1.
  - TC-FA-CF-598 tidak menyebut cara membuktikan "kedua Save sukses tanpa dialog konflik" selain toast; spec mengasersi ketiadaan dialog konflik per sesi.
