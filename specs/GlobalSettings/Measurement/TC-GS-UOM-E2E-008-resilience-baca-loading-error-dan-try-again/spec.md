---
id: TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca: Loading, Error Load, dan Try Again pada Tabel, Changelog, dan Unit Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-9
  - TC-GS-UOM-13
  - TC-GS-UOM-14
  - TC-GS-UOM-305
  - TC-GS-UOM-362
coverage:
  web: automated
---

# Resilience Baca: Loading, Error Load, dan Try Again pada Tabel, Changelog, dan Unit Detail

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data (hanya dibaca, spec tidak membuat atau mengubah data backend): Pre-setup Client A dan Population D-01 (di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md`), sehingga halaman 1 berisi 10 baris. Unit Pieces (3 baris Item Type List) dipakai untuk Modal Unit Detail dan dicari lewat Search karena berada di halaman 2.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit; nama endpoint konkret ditentukan tim FE di tahap script dari kontrak modul:
  - Respons daftar Measurement: tahan 3 detik lalu jawab normal (langkah 1 sampai 7, TC-GS-UOM-9; lamanya adalah parameter Data Uji "Delay: 3 detik"); jawab 500 (langkah 8 sampai 12, TC-GS-UOM-13). Intercept 500 yang sama dilepas di langkah 13 sebelum [Try Again] (TC-GS-UOM-14); tidak dibutuhkan intercept "500 sekali" terpisah.
  - Respons daftar Changelog Measurement: jawab 500 (langkah 18, TC-GS-UOM-305); dilepas di langkah 22 sebelum [Try Again].
  - Respons data Detail Unit: tahan 3 detik (langkah 27, TC-GS-UOM-362); jawab 500 (langkah 33); dilepas di langkah 37 sebelum [Try Again].
- Guided Tooltip: flag halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Pemulihan di hook `after`: semua intercept dilepas walau spec gagal di tengah. Spec tidak mengubah data backend.

## Test Steps

### TC-GS-UOM-9: Tampilan Loading saat data tabel diambil

1. Pasang intercept pada respons daftar Measurement: tahan 3 detik
2. Buka Global Settings > Master Reference > Measurement (muat ulang halaman)
3. Verifikasi Skeleton loader / Loading component tampil pada area tabel
4. Tunggu respons diterima
5. Verifikasi data tabel tampil
6. Verifikasi Skeleton loader / Loading component hilang
7. Lepas intercept respons daftar Measurement

### TC-GS-UOM-13: Error Load tabel saat pengambilan data gagal

8. Pasang intercept pada respons daftar Measurement: jawab 500
9. Buka Global Settings > Master Reference > Measurement (muat ulang halaman)
10. Verifikasi area tabel menampilkan `Unable to load this data.`
11. Verifikasi area tabel menampilkan `[Try Again]`
12. Verifikasi tidak ada baris data parsial di tabel

### TC-GS-UOM-14: Klik Try Again memuat ulang data setelah Error Load

13. Pulihkan respons normal pada respons daftar Measurement (lepas intercept 500 dari TC-GS-UOM-13)
14. Klik [Try Again]
15. Verifikasi Loading tampil
16. Verifikasi data tabel termuat dengan 10 baris di halaman 1
17. Verifikasi pesan error `Unable to load this data.` hilang

### TC-GS-UOM-305: Error Load Modal Changelog menampilkan pesan error dan Try Again, bukan empty state

18. Pasang intercept pada respons daftar Changelog Measurement: jawab 500
19. Klik icon Changelog
20. Verifikasi Modal Changelog menampilkan `Unable to load this data.`
21. Verifikasi Modal Changelog menampilkan `[Try Again]`
22. Pulihkan respons normal pada respons daftar Changelog Measurement
23. Verifikasi Modal Changelog tidak menampilkan empty state `No changelog yet`
24. Klik [Try Again]
25. Verifikasi data Changelog termuat
26. Tutup Modal Changelog lewat `✕` di header

### TC-GS-UOM-362: Loading dan Error Load pada Modal Unit Detail

27. Pasang intercept pada respons data Detail Unit: tahan 3 detik
28. Ketik Search `Pieces`, tekan Enter
29. Klik `⋯` baris Pieces > Detail
30. Verifikasi Modal Unit Detail menampilkan Skeleton loader / Loading component saat data diambil
31. Tunggu respons diterima
32. Tutup Modal Unit Detail lewat `[✕]`
33. Ganti intercept respons data Detail Unit: jawab 500
34. Klik `⋯` baris Pieces > Detail
35. Verifikasi Modal Unit Detail menampilkan `Unable to load this data.`
36. Verifikasi Modal Unit Detail menampilkan `[Try Again]`
37. Pulihkan respons normal pada respons data Detail Unit
38. Klik [Try Again]
39. Verifikasi Modal Unit Detail Pieces menampilkan 3 baris Item Type List
40. Tutup Modal Unit Detail lewat `[✕]`
41. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (intercept parsial, kelas harness fault injection; bagian 6 konvensi). Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini sekitar 41 langkah, di atas batas 35 langkah: seluruh blok satu kelas harness (fault injection baca), satu akun, tanpa membuat data, dan tiap blok (tabel, Changelog, Unit Detail) berdiri sendiri.
- TC-GS-UOM-14 berdependensi TC-GS-UOM-13, dan langkah 1 sampai 2 TC-GS-UOM-14 (paksa 500, buka Tab Measurement) identik dengan langkah 8 dan 9 spec ini; spec melanjutkan state Error Load dari TC-GS-UOM-13 tanpa membuka ulang tab, lalu memulihkan respons di langkah 13 sebelum [Try Again].
- Langkah 15 mengasersi Loading segera setelah klik [Try Again], sebelum data termuat (state sementara, S-09 butir 5).
- Langkah 23 mewujudkan klausa "bukan empty state `No changelog yet`" pada Expected a TC-GS-UOM-305; diasersi setelah respons dipulihkan dan sebelum [Try Again], saat pesan error masih menjadi isi modal.
- Pada TC-GS-UOM-362 langkah uji 2 (buka Detail dengan respons ditahan) dan langkah uji 3 (paksa 500, tutup, buka lagi) dipetakan ke langkah 27 sampai 34: modal dibuka dengan respons ditahan 3 detik (loader), dimuat penuh, ditutup, lalu dibuka lagi dengan respons 500.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 (menunggu respons), 7 dan 13 dan 22 dan 37 (melepas atau memulihkan respons), 28 dan 41 (Search `Pieces` untuk menemukan baris di halaman 2 dan mengosongkannya), 31 (menunggu respons Detail), 26 dan 32 dan 40 (menutup modal), 33 (mengganti intercept dari tahan ke 500).
- Nama endpoint tidak disebut di TC sumber; kebutuhan ini sudah dicatat di Prerequisites.
- Spec ini berdiri terpisah dari `TC-GS-UOM-E2E-009-resilience-export-gagal-download` karena gabungan keduanya 64 langkah (41 + 23), jauh melewati batas 35 langkah; spec ini hanya memakai intercept respons baca (tabel, Changelog, Unit Detail), sedangkan 009 memakai intercept respons export dan penyuntikan kegagalan pembuatan file di browser. Tiap spec membuka layar dan modalnya sendiri, sehingga kegagalan satu spec tidak membuat spec lain kehilangan makna.
- Temuan untuk QA: TC-GS-UOM-362 langkah uji 1 menahan respons Detail lalu langkah uji 3 memaksa 500, tanpa menyebut apakah respons yang ditahan kemudian dijawab normal atau 500; spec menjawab normal pada pembukaan pertama (loader teramati lalu data termuat) dan 500 pada pembukaan kedua.
