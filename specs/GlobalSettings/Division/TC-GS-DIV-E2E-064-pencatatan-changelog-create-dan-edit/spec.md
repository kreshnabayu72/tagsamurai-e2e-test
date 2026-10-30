---
id: TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit
title: "Pencatatan Changelog: Entri Create dan Edit (Name, Code, Name+Code, Rename)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-235
  - TC-GS-DIV-236
  - TC-GS-DIV-237
  - TC-GS-DIV-238
  - TC-GS-DIV-239
  - TC-GS-DIV-241
  - TC-GS-DIV-245
  - TC-GS-DIV-249
coverage:
  web: automated
---

# Pencatatan Changelog: Entri Create dan Edit (Name, Code, Name+Code, Rename)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (6 Division) tidak dipakai dan tidak diubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi; seluruh Division di bawah milik spec ini):
  - `Log Create {runId}-064` dengan Code `LGC`: dibuat spec lewat UI pada TC-GS-DIV-235; di-rename menjadi `Log Create Renamed {runId}-064` pada TC-GS-DIV-237 (setara dependensi TC-GS-DIV-235); Code diubah `LGC` menjadi `LGC2` pada TC-GS-DIV-238 (setara dependensi TC-GS-DIV-237).
  - `Log Generate {runId}-064` dengan Code dikosongkan (Code hasil auto-generate dicatat dari tabel): dibuat spec lewat UI pada TC-GS-DIV-236; diubah menjadi Name `Log Gen 2` dan Code `LG9` pada TC-GS-DIV-239 (setara dependensi TC-GS-DIV-236); Code dikosongkan pada TC-GS-DIV-241 sehingga di-generate `LG2` (setara dependensi TC-GS-DIV-239). Name `Log Gen 2` bernama literal tanpa suffix karena Code hasil auto-generate `LG2` pada TC-GS-DIV-241 bergantung pada Name itu (bagian 5 konvensi, S-12).
  - `Metro Branch {runId}-064` dengan Code `MTB` (D-15): dibuat spec lewat UI pada TC-GS-DIV-245, di-rename menjadi `Metro Branch 2 {runId}-064` lalu `Metro Branch 3 {runId}-064`.
  - `Log Delete {runId}-064`: Division bebas relasi, di-seed lewat API di hook `before`, dihapus lewat API pada langkah TC-GS-DIV-249 (setara dependensi TC-GS-DIV-242) supaya Changelog memuat entri Delete.
- Kode literal `LGC`, `LGC2`, `LG9`, `LG2`, dan `MTB` mengikuti TC dan unik per entitas. Hook `before` menghapus lewat API sisa Division milik spec ini dari run sebelumnya (nama berakhiran `-064` atau bernama `Log Gen 2`; penghapusan dibatasi ke nama itu, bukan berdasarkan kode saja) sehingga kode itu bebas, termasuk `LG2` yang harus belum dipakai pada TC-GS-DIV-241.
- Kemampuan teknis: seeding Division lewat API dan penghapusan Division lewat API (sesi API aktor Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division milik spec ini yang masih ada: `Log Create {runId}-064`, `Log Create Renamed {runId}-064`, `Log Generate {runId}-064`, `Log Gen 2`, `Metro Branch {runId}-064`, `Metro Branch 2 {runId}-064`, `Metro Branch 3 {runId}-064`, dan `Log Delete {runId}-064`. Entri Changelog bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Tidak ada state global yang diubah.
- TC-GS-DIV-235, 236, 237, 238, 239, 241, 245, 249: login sebagai Total Control dan berada di Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-235: Create dengan Code manual mencatat satu entri Division Name saja

1. Klik [+ Division], isi Division Name `Log Create {runId}-064` dan Code `LGC`, klik [Submit]
2. Tunggu aksi selesai (modal Create tertutup)
3. Buka Modal Changelog, ketik Search `Log Create {runId}-064`, tekan Enter
4. Verifikasi Changelog: tepat 1 entri dengan Action `Create`, Division Name `Log Create {runId}-064`, Field `Division Name`, Old Value `—`, New Value `Log Create {runId}-064`, Modified By `Sari D`
5. Verifikasi Changelog tidak memuat entri Field `Code` untuk `Log Create {runId}-064`
6. Tutup Modal Changelog, buka Global Settings > Activity Log, ketik Search `Log Create {runId}-064`, tekan Enter
7. Verifikasi Activity Log: tepat 1 entri dengan Action `Create`, Object `Division`, Name `Log Create {runId}-064`, Field `Division Name`, Old Value `—`, New Value `Log Create {runId}-064`

### TC-GS-DIV-236: Create dengan Code di-generate mencatat satu entri Division Name saja

8. Buka Global Settings > User > Division, klik [+ Division], isi Division Name `Log Generate {runId}-064`, biarkan Code kosong, klik [Submit]
9. Tunggu aksi selesai (modal Create tertutup)
10. Ketik Search `Log Generate {runId}-064`, tekan Enter pada tabel Division, catat Code baris sebagai `{codeGenerate}` (Code hasil auto-generate)
11. Buka Modal Changelog, ketik Search `Log Generate {runId}-064`, tekan Enter
12. Verifikasi Changelog: hanya 1 entri `Create` untuk `Log Generate {runId}-064` dengan Field `Division Name`
13. Verifikasi Code hasil auto-generate `{codeGenerate}` tidak dicatat sebagai entri terpisah: tidak ada entri Field `Code` untuk `Log Generate {runId}-064`

### TC-GS-DIV-237: Edit hanya Name mencatat satu entri Field Division Name

14. Tutup Modal Changelog, ganti isi kotak search tabel Division dengan `Log Create {runId}-064`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Log Create Renamed {runId}-064`, klik [Save]
15. Tunggu aksi selesai (modal Edit tertutup)
16. Buka Modal Changelog, ketik Search `Log Create Renamed {runId}-064`, tekan Enter
17. Verifikasi Changelog: tepat 1 entri dengan Action `Edit`, Division Name `Log Create Renamed {runId}-064` (nama sesudah rename), Field `Division Name`, Old Value `Log Create {runId}-064`, New Value `Log Create Renamed {runId}-064`, Modified By `Sari D`
18. Verifikasi Changelog tidak memuat entri Field `Code` untuk `Log Create Renamed {runId}-064`

### TC-GS-DIV-238: Edit hanya Code mencatat satu entri Field Code

19. Tutup Modal Changelog, ganti isi kotak search tabel Division dengan `Log Create Renamed {runId}-064`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Code `LGC` menjadi `LGC2`, klik [Save]
20. Tunggu aksi selesai (modal Edit tertutup)
21. Buka Modal Changelog, ketik Search `Log Create Renamed {runId}-064`, tekan Enter
22. Verifikasi Changelog: tepat 1 entri dengan Action `Edit`, Field `Code`, Old Value `LGC`, New Value `LGC2`
23. Verifikasi Changelog tidak memuat entri Field `Division Name` baru: hasil Search tetap memuat tepat 1 entri Field `Division Name`, yaitu entri rename TC-GS-DIV-237

### TC-GS-DIV-239: Edit Name dan Code sekaligus mencatat dua entri terpisah

24. Ganti isi kotak search Changelog dengan `Log Gen 2`, tekan Enter, catat jumlah entri sebagai `{n239}`
25. Tutup Modal Changelog, ganti isi kotak search tabel Division dengan `Log Generate {runId}-064`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Log Gen 2` dan Code menjadi `LG9`, klik [Save]
26. Tunggu aksi selesai (modal Edit tertutup)
27. Buka Modal Changelog, ketik Search `Log Gen 2`, tekan Enter
28. Verifikasi Changelog: jumlah entri `Log Gen 2` bertambah tepat 2 dari `{n239}`, keduanya Action `Edit`
29. Verifikasi Changelog: satu entri baru Field `Division Name` dengan Old Value `Log Generate {runId}-064` dan New Value `Log Gen 2`
30. Verifikasi Changelog: satu entri baru Field `Code` dengan Old Value `{codeGenerate}` dan New Value `LG9`
31. Verifikasi Changelog tidak memuat entri ganda untuk field yang sama: Field `Division Name` dan Field `Code` masing-masing tepat 1 entri baru
32. Catat jumlah entri Field `Division Name` pada hasil Search `Log Gen 2` sebagai `{dn239}`

### TC-GS-DIV-241: Edit dengan Code dikosongkan mencatat entri Code bila berbeda

33. Tutup Modal Changelog, ganti isi kotak search tabel Division dengan `Log Gen 2`, tekan Enter, klik `⋯` pada baris tersebut > Edit, kosongkan Code, klik [Save]
34. Tunggu aksi selesai (modal Edit tertutup)
35. Buka Modal Changelog, ketik Search `Log Gen 2`, tekan Enter
36. Verifikasi Changelog: jumlah entri `Log Gen 2` bertambah tepat 1 dari sesudah TC-GS-DIV-239 (`{n239}` + 2), yaitu entri Action `Edit`, Field `Code`, Old Value `LG9`, New Value `LG2` (hasil auto-generate dari Name `Log Gen 2`)
37. Verifikasi Changelog tidak memuat entri Field `Division Name` baru: jumlah entri Field `Division Name` untuk `Log Gen 2` tetap `{dn239}`

### TC-GS-DIV-245: Entri Changelog lama tidak berubah setelah rename berikutnya

38. Tutup Modal Changelog, klik [+ Division], isi Division Name `Metro Branch {runId}-064` dan Code `MTB`, klik [Submit]
39. Tunggu aksi selesai (modal Create tertutup)
40. Ganti isi kotak search tabel Division dengan `Metro Branch {runId}-064`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Metro Branch 2 {runId}-064`, klik [Save]
41. Tunggu aksi selesai (modal Edit tertutup)
42. Ganti isi kotak search tabel Division dengan `Metro Branch 2 {runId}-064`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Division Name menjadi `Metro Branch 3 {runId}-064`, klik [Save]
43. Tunggu aksi selesai (modal Edit tertutup)
44. Buka Modal Changelog, ketik Search `Metro Branch`, tekan Enter
45. Verifikasi Changelog: entri rename pertama tetap Action `Edit`, Division Name `Metro Branch 2 {runId}-064`, Old Value `Metro Branch {runId}-064`, New Value `Metro Branch 2 {runId}-064`
46. Verifikasi Changelog: entri rename kedua Action `Edit`, Division Name `Metro Branch 3 {runId}-064`, Old Value `Metro Branch 2 {runId}-064`, New Value `Metro Branch 3 {runId}-064`
47. Verifikasi entri rename pertama tidak ter-overwrite oleh nilai terbaru: New Value tetap `Metro Branch 2 {runId}-064`, bukan `Metro Branch 3 {runId}-064`

### TC-GS-DIV-249: Old Value dan New Value tidak pernah keduanya strip pada satu entri

48. Hapus Division `Log Delete {runId}-064` lewat API (sesi API aktor Total Control)
49. Tutup lalu buka lagi Modal Changelog dengan Search kosong dan urutan default (Newest First), lihat halaman pertama
50. Verifikasi Changelog halaman pertama menampilkan entri dengan Action `Create`, `Edit`, dan `Delete` (sedikitnya satu entri tiap Action)
51. Verifikasi Changelog halaman pertama: setiap entri `Create` memiliki Old Value `—` dan New Value terisi nama Division
52. Verifikasi Changelog halaman pertama: setiap entri `Edit` memiliki Old Value dan New Value keduanya terisi
53. Verifikasi Changelog halaman pertama: setiap entri `Delete` memiliki Old Value terisi dan New Value `—`
54. Verifikasi Changelog halaman pertama tidak memuat entri dengan Old Value dan New Value sama-sama `—`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Urutan TC di spec: 235, 236, 237, 238, 239, 241, 245, 249. 237 sesudah 235 dan 238 sesudah 237 mengikuti rantai dependensi TC (Division yang sama); 239 sesudah 236 dan 241 sesudah 239 mengikuti rantai kedua. 249 paling akhir karena memerlukan entri Create, Edit, dan Delete sekaligus pada halaman pertama.
- Dependensi TC-GS-DIV-235, 236, 237, 238, 239 dijalankan sebagai langkah di spec ini, bukan bergantung pada spec lain. Dependensi TC-GS-DIV-242 (entri Delete untuk TC-GS-DIV-249) dijalankan lewat penghapusan API pada langkah 48 supaya entri Delete menjadi entri terbaru dan masuk halaman pertama; aksi Delete lewat UI diuji di spec `TC-GS-DIV-E2E-065-pencatatan-changelog-delete-dan-bulk-delete`.
- Entri Changelog dikenali lewat nama bersuffix `{runId}-064`; entri milik run lain diabaikan. `Log Gen 2` bernama literal sehingga entri run lain dengan nama itu ikut tampil di Search; asersi pada langkah 28, 36, dan 37 memakai selisih jumlah entri terhadap `{n239}` atau `{dn239}` (baseline, S-12), bukan posisi teratas.
- Klausa "tidak ada entri Field `Code`" atau "tidak ada entri Field `Division Name`" pada Expected Result b TC-GS-DIV-235, 236, 237, 238, dan 241 ditulis sebagai asersi jumlah entri pada hasil Search yang sama dengan entri yang baru diverifikasi (anchor positif pada langkah 4, 12, 17, 22, 36); ini asersi jumlah pada aksi yang berhasil, bukan asersi absence kelas g (aksi gagal atau No-Op ada di spec `TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use`).
- Langkah penghubung (aksi tanpa `Verifikasi`): menutup Modal Changelog dan Search nama Division pada tabel Division sebelum aksi Edit (langkah 14, 19, 25, 33, 40, 42), ganti Search Changelog dan mencatat `{n239}` (langkah 24), mencatat `{dn239}` (langkah 32), mencatat Code hasil auto-generate (langkah 10), kembali ke tab Division (langkah 8), menutup lalu membuka lagi Modal Changelog (langkah 49), serta langkah 2, 9, 15, 20, 26, 34, 39, 41, dan 43 (menunggu aksi [Submit] atau [Save] selesai sebelum aksi berikutnya, 8b butir 8). Search pada tabel Division adalah bagian dari langkah aksi yang sama (tabel A-Z dengan lebih dari satu halaman, sehingga baris bersuffix tidak dijamin tampil di halaman 1).
- TC-GS-DIV-239 Expected Result a menyebut "kode lama" tanpa nilai; spec memakai Code hasil auto-generate `Log Generate {runId}-064` yang dicatat pada langkah 10. Toast sukses tidak diasersi karena tidak ada di Expected Result TC-GS-DIV-235 sampai 249.
- TC-GS-DIV-249 Langkah Uji 1 menyatakan "halaman pertama"; halaman pertama berurutan Newest First memuat entri Create, Edit, dan Delete hasil langkah 1 sampai 48.
- Spec melewati sekitar 35 langkah (54 langkah) karena delapan TC membentuk dua rantai dependensi Division yang sama (TC-GS-DIV-235 ke 237 ke 238, dan TC-GS-DIV-236 ke 239 ke 241) dalam satu kelas harness (pencatatan Changelog); memecahnya berarti menyalin langkah dependensi ke spec lain. Blok baca-log berpola (buka Modal Changelog, Search, `Verifikasi` kolom log) mendominasi jumlah langkah. Dua rantai dependensi dalam satu kelas harness: blok dalam rantai yang sama melanjutkan Division yang dibuat blok sebelumnya (237 dan 238 bergantung pada 235; 239 dan 241 pada 236), sedangkan blok 245 membuat Division milik sendiri dan blok 249 membaca entri Create, Edit, dan Delete hasil blok-blok sebelumnya pada halaman pertama Changelog (bergantung pada langkah 1 sampai 48).
- Temuan untuk QA:
  - TC-GS-DIV-245 Post Condition ("Division Metro Branch 3 (Code MTB) tersimpan (D-15)") tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-GS-DIV-249 mensyaratkan entri Delete dari TC-GS-DIV-242 yang berada di spec lain; spec ini men-seed entri itu lewat penghapusan API (cara lain tidak didefinisikan TC) sehingga Modified By entri Delete itu bukan `Sari D` bila sesi API memakai akun lain, dan hal itu tidak diasersi.
  - TC-GS-DIV-241 Precondition menyatakan "Code `LG2` belum dipakai" tanpa cara menjamin; spec mengandalkan hook `before` yang membersihkan sisa Division spec ini.
  - TC-GS-DIV-239 Expected Result b ("Tidak ada entri ganda untuk field yang sama") tidak menyebut cara membedakan entri ganda dari entri run lain; spec memakai selisih jumlah entri terhadap `{n239}`.
