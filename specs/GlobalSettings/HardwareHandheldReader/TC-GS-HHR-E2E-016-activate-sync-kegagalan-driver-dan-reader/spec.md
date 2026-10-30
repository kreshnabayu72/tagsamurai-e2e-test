---
id: TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader
title: "Sync Activate Reader: Spinner, Driver Tidak Terpasang, Reader Mati, Kabel Dicabut, Dua Reader Tersambung, dan Sync Ulang yang Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-58
  - TC-GS-HHR-59
  - TC-GS-HHR-60
  - TC-GS-HHR-61
  - TC-GS-HHR-62
  - TC-GS-HHR-465
coverage:
  web: automated
---

# Sync Activate Reader: Spinner, Driver Tidak Terpasang, Reader Mati, Kabel Dicabut, Dua Reader Tersambung, dan Sync Ulang yang Gagal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai simulator reader USB bersama dan membaca Event Log Activate Client A yang ditulis spec lain.
- Aktor: Total Control Sari Dewi (Client A) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup: Client A plan Growth, Seed Reader A DD-01 s.d. DD-10, Seed Event Log Client A EL-01 s.d. EL-05 (dipakai sebagai baris pembanding), Hardware Stock Principal HS-01 (`SN-HHR-00201`, Long Range, Current Power 22 dBm). State awal dipulihkan fixture backend sebelum spec (Catatan TC; mekanisme disediakan tim FE/BE).
- Spec tidak mengirim `[Submit]`: tidak ada reader, stok, atau kuota yang berubah, sehingga tidak ada pemulihan data.
- Kemampuan teknis: simulator reader USB dan driver lokal (disediakan tim FE; mekanisme tidak didefinisikan di TC, PRD, atau LLD) dengan kondisi yang dapat diatur per langkah:
  - driver lokal reader belum terpasang;
  - kabel USB terpasang, reader mati, driver terpasang;
  - reader `SN-HHR-00201` tersambung, driver terpasang, dengan pembacaan dapat ditahan agar spinner teramati dan kabel dapat dicabut saat pembacaan berlangsung;
  - dua reader tersambung bersamaan;
  - pencabutan kabel reader.
- Kemampuan teknis tambahan: pembacaan jumlah total baris popup Event Log Activate (baseline, S-12).
- Cleanup (hook `after`): tutup popup yang masih terbuka dan pulihkan simulator ke kondisi awal (tanpa reader tersambung, driver terpasang).

## Test Steps

### Baseline Event Log Activate

1. Klik ikon Event Log
2. Catat jumlah total baris popup Event Log Activate sebagai baseline
3. Tutup popup Event Log lewat `[✕]`

### TC-GS-HHR-62: Dua reader tersambung bersamaan saat Sync

4. Klik `[+ Activate Reader]`
5. Klik `Long Range` pada Overlay `Select Range Type`
6. Atur simulator: dua reader USB tersambung bersamaan
7. Klik `[Sync]`
8. Verifikasi banner inline dekat `[Sync]`: `Connect only one reader at a time.`
9. Verifikasi `Serial Number` tetap kosong
10. Verifikasi `[Submit]` disabled
11. Verifikasi `[Sync]` tetap dapat diklik
12. Klik `[✕]` di header popup Activate
13. Klik ikon Event Log
14. Verifikasi sedikitnya satu baris tampil di popup Event Log Activate
15. Verifikasi jumlah total baris popup Event Log Activate sama dengan baseline pada langkah 2 (tidak ada baris baru)
16. Tutup popup Event Log lewat `[✕]`

### TC-GS-HHR-59: Driver USB tidak terpasang

17. Klik `[+ Activate Reader]`
18. Klik `Long Range` pada Overlay `Select Range Type`
19. Atur simulator: driver lokal reader belum terpasang
20. Klik `[Sync]`
21. Verifikasi banner inline di Popup Activate dekat `[Sync]`: `USB driver not detected. Please install the reader driver software.`
22. Verifikasi `Serial Number` tetap kosong
23. Verifikasi `[Submit]` disabled
24. Verifikasi popup tetap terbuka

### TC-GS-HHR-60: Reader mati saat Sync

25. Atur simulator: kabel USB terpasang, reader dalam keadaan mati, driver terpasang
26. Klik `[Sync]`
27. Verifikasi banner inline dekat `[Sync]`: `Reader not responding. Ensure device is powered on and cable connected securely.`
28. Verifikasi `[Submit]` disabled
29. Verifikasi `[Sync]` tetap dapat diklik

### TC-GS-HHR-61: Kabel dicabut saat nomor seri sedang dibaca

30. Atur simulator: reader `SN-HHR-00201` tersambung, driver terpasang, pembacaan ditahan
31. Klik `[Sync]`
32. Cabut kabel USB saat spinner tampil
33. Verifikasi muncul toast error: "Error, failed to read serial number. Reconnect the cable and click Sync again."
34. Verifikasi `Serial Number` tetap kosong
35. Verifikasi `[Sync]` aktif kembali

### TC-GS-HHR-58: Tombol Sync menampilkan spinner saat membaca nomor seri

36. Atur simulator: reader `SN-HHR-00201` tersambung, driver terpasang, pembacaan ditahan
37. Klik `[Sync]`
38. Verifikasi tombol `[Sync]` menampilkan state loading dengan animasi spinner selama pembacaan Serial Number
39. Lepaskan tahanan pembacaan di simulator
40. Verifikasi spinner pada `[Sync]` hilang
41. Verifikasi `Serial Number` terisi `SN-HHR-00201`

### TC-GS-HHR-465: Sync ulang yang gagal mengosongkan hasil Sync sebelumnya

42. Cabut kabel USB reader `SN-HHR-00201`
43. Klik `[Sync]`
44. Verifikasi banner inline dekat `[Sync]`: `Reader not responding. Ensure device is powered on and cable connected securely.`
45. Verifikasi `Serial Number`, label jalur, `Device Name`, `SKU`, `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` tidak tampil (popup kembali ke state Menunggu Sync)
46. Verifikasi `[Submit]` disabled
47. Verifikasi `[Sync]` tetap dapat diklik
48. Klik `[✕]` di header popup Activate

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Kelas harness: eksternal (d), simulator reader USB; seluruh TC berlabel Manual Only (b) di TC sumber. Satu kelas harness, satu topik (kegagalan dan state Sync), satu akun.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan blok menyimpang dari urutan nomor TC: TC-GS-HHR-62 pertama karena asersi jumlah baris Event Log memakai baseline (langkah 2) yang harus diambil sebelum Sync gagal lain berjalan dan tidak boleh tercampur oleh blok sesudahnya; blok TC-GS-HHR-59, TC-GS-HHR-60, TC-GS-HHR-61, TC-GS-HHR-58, dan TC-GS-HHR-465 memakai satu popup (satu pembukaan, tanpa submit; prinsip 13, halaman yang sama dipakai berulang) dengan kondisi simulator diatur ulang tiap blok. Urutan 58 sebelum 465 karena TC-GS-HHR-465 membutuhkan hasil Sync berhasil (`SN-HHR-00201`) dari TC-GS-HHR-58.
- Spec melewati sekitar 35 langkah (48 langkah). Alasan: 23 langkah adalah `Verifikasi` yang dipecah per klausa Expected (S-01); semua blok satu kelas harness dan satu popup, tiap blok mengatur ulang kondisi simulator sehingga kegagalan satu kondisi tidak membuat kondisi lain kehilangan makna, dan tidak ada data yang dibuat.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 sampai 3 (baseline), langkah 6, 19, 25, 30, 36, 39, dan 42 (mengatur simulator), langkah 12, 16, dan 48 (menutup popup tanpa hasil Sync; langkah 48 menutup popup yang sudah kembali ke state Menunggu Sync pada TC-GS-HHR-465), dan langkah 32 (pencabutan kabel adalah pemicu TC-GS-HHR-61).
- Asersi "tidak ada baris baru" (TC-GS-HHR-62 Expected c, langkah 15) ditulis sebagai selisih jumlah total baris terhadap baseline dengan anchor positif pada langkah 14 (S-12, butir 2 bagian 8b). TC-GS-HHR-62 tidak ada di `sourceTc` spec absence mana pun, sehingga `Verifikasi` berbaseline ditulis di sini. P-1 (state berat): kondisi dua reader tersambung bersamaan adalah state harness yang dibangun langkah 6 pada spec ini dan tidak bisa diulang di spec lain tanpa biaya yang sama; asersi itu tetap berada di spec asalnya.
- Langkah 33 (toast) diasersi sebelum langkah 34 dan 35 karena toast bersifat sementara; langkah 38 (spinner) diasersi sebelum tahanan dilepas (butir 5 bagian 8b).
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (driver tidak terpasang, reader mati, kabel dicabut, dua reader, penahanan pembacaan) tidak didefinisikan di TC, PRD, atau LLD; spec mencatat kebutuhan di Prerequisites tanpa mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-59, TC-GS-HHR-60, TC-GS-HHR-61, dan TC-GS-HHR-62 menulis "`Serial Number` tetap kosong" sedangkan NC-15 dan TC-GS-HHR-465 menyatakan field `Serial Number` tidak tampil sebelum Sync berhasil; spec mengikuti kata TC (langkah 9, 22, 34) dan QA diminta memastikan apakah maksudnya kosong atau tidak tampil.
  - TC-GS-HHR-62 Expected c ("Tidak ada baris baru di Popup Event Log Activate") tidak menyebut kondisi baseline; spec memakai jumlah total baris sebelum Sync pertama (langkah 2). TC-GS-HHR-59, TC-GS-HHR-60, TC-GS-HHR-61, dan TC-GS-HHR-465 tidak punya Expected tentang Event Log, sehingga pencatatan Event Log untuk kegagalan itu tidak diasersi.
  - TC-GS-HHR-61 tidak menyebut kondisi "pembacaan ditahan" pada simulator agar spinner teramati saat kabel dicabut; kebutuhan itu ditulis di Prerequisites.
  - TC-GS-HHR-465 langkah 4 ("Cabut kabel USB lalu klik `[Sync]` lagi") memakai Sync pertama yang berhasil sebagai prasyarat; spec memakai hasil Sync berhasil dari blok TC-GS-HHR-58 sebagai prasyarat itu (langkah 37 sampai 41), bukan Sync terpisah.
  - Perilaku banner lama saat Sync berikutnya gagal dengan penyebab berbeda (banner diganti atau ditumpuk) tidak dinyatakan di TC; spec mengasersi hanya banner yang diharapkan tiap blok. Bila banner lama bertahan, QA perlu menyatakannya agar blok dapat dipecah.
