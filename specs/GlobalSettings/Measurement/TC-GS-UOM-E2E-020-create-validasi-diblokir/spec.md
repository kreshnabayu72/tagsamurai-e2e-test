---
id: TC-GS-UOM-E2E-020-create-validasi-diblokir
title: "Validasi Create Unit yang Diblokir: Kosong, Spasi, Batas, Emoji, Duplikat, dan Aksesibilitas Error"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-39
  - TC-GS-UOM-40
  - TC-GS-UOM-43
  - TC-GS-UOM-44
  - TC-GS-UOM-46
  - TC-GS-UOM-47
  - TC-GS-UOM-48
  - TC-GS-UOM-51
  - TC-GS-UOM-52
  - TC-GS-UOM-335
coverage:
  web: automated
---

# Validasi Create Unit yang Diblokir: Kosong, Spasi, Batas, Emoji, Duplikat, dan Aksesibilitas Error

## Prerequisites

- Mode: FE+BE (backend nyata; TC-GS-UOM-46, 47, dan 48 butuh pengecekan keunikan nama ke backend).
- Hook suite (login akun default Total Control Client A, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`. Password dari `Spectra.env.GS_TC_PASSWORD`; tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (data baca, tidak diubah spec): `Kilogram` (TC-GS-UOM-46), `Meter` (TC-GS-UOM-47), dan `Liter` (TC-GS-UOM-48) sebagai nama yang sudah ada.
- Data uji: semua nilai hanya diketik dan seluruh submit diblokir, sehingga tidak ada unit yang dibuat dan tidak ada seeding. Nilai yang dibangkitkan skrip: Unit Name 121 karakter huruf biasa (TC-GS-UOM-43); `Emoji Sym {runId}-020` sebagai Unit Name pendamping Symbol berisi emoji (TC-GS-UOM-52); Symbol `x`/`bx` sebagai pengisi Symbol agar penyebab blokir hanya field yang diuji.
- Hook `afterEach`: tutup modal Create yang masih terbuka dan dirty lewat `[✕]`, lalu klik [Leave] pada dialog `Unsaved Changes`, kembali ke layar Measurement (cadangan bila langkah 59 sampai 61 tidak tercapai).
- Cleanup (hook `after`, tidak berasumsi langkah UI berhasil penuh): bila ada unit tak terduga yang terbentuk dengan nama dari spec ini (mis. `Box 📦`, `Emoji Sym {runId}-020`), hapus lewat API.
- Kemampuan teknis: pengetikan karakter per karakter; penantian debounce ±500 ms; pembacaan nilai field, jumlah karakter, dan atribut ARIA (`aria-required`, `aria-describedby`); klik [Submit] dalam kurang dari 500 ms setelah mengetik (TC-GS-UOM-48); pengecekan daftar Measurement lewat API.
- State global: tidak ada yang diubah. Sesi tetap di akun default suite.

## Test Steps

### TC-GS-UOM-39 dan TC-GS-UOM-335: Submit Create dengan Unit Name dan Symbol kosong, serta aksesibilitas field

1. Klik [+ Unit]
2. Verifikasi field Unit Name memiliki `aria-required="true"`
3. Verifikasi field Symbol memiliki `aria-required="true"`
4. Klik [Submit] dengan kedua field kosong
5. Verifikasi error inline Unit Name `Unit name must not be empty` tampil
6. Verifikasi error inline Symbol `Symbol must not be empty` tampil
7. Verifikasi modal tetap terbuka
8. Verifikasi field Unit Name memiliki `aria-describedby` yang menunjuk elemen pesan error miliknya
9. Verifikasi field Symbol memiliki `aria-describedby` yang menunjuk elemen pesan error miliknya
10. Tekan Tab berulang melewati elemen terakhir
11. Verifikasi fokus Tab berputar hanya di dalam popup dan tidak keluar ke halaman di belakang

### TC-GS-UOM-40: Submit Create dengan Unit Name dan Symbol hanya spasi

12. Klik [Clear Field]
13. Isi Unit Name 3 spasi, Symbol 2 spasi
14. Klik [Submit]
15. Verifikasi error inline Unit Name `Unit name must not be empty` tampil
16. Verifikasi error inline Symbol `Symbol must not be empty` tampil

### TC-GS-UOM-43: Unit Name 121 karakter

17. Klik [Clear Field]
18. Ketik Unit Name 121 karakter huruf biasa
19. Verifikasi field Unit Name menerima karakter ke-121 (panjang nilai field 121 karakter)
20. Verifikasi error inline `Max. 120 characters` tampil saat melebihi
21. Isi Symbol `x`
22. Klik [Submit]
23. Verifikasi Submit diblokir (modal tetap terbuka)

### TC-GS-UOM-44: Unit Name berisi emoji

24. Klik [Clear Field]
25. Ketik Unit Name `Box 📦`
26. Verifikasi error inline `Unit name contains invalid characters` tampil saat mengetik
27. Isi Symbol `bx`
28. Klik [Submit]
29. Verifikasi Submit diblokir (modal tetap terbuka)

### TC-GS-UOM-46: Unit Name duplikat tanpa membedakan huruf besar kecil

30. Klik [Clear Field]
31. Ketik Unit Name `KILOGRAM`
32. Tunggu ±500 ms tanpa memindahkan fokus
33. Verifikasi error inline `Unit name already exists` muncul saat mengetik, tanpa menunggu fokus keluar field
34. Isi Symbol `x`
35. Klik [Submit]
36. Verifikasi Submit menolak dengan error inline `Unit name already exists`

### TC-GS-UOM-47: Unit Name duplikat dengan spasi depan dan belakang tetap terdeteksi

37. Klik [Clear Field]
38. Ketik Unit Name `  meter ` (2 spasi depan, 1 spasi belakang)
39. Tunggu debounce ±500 ms
40. Verifikasi error inline `Unit name already exists` tampil
41. Isi Symbol `x`
42. Klik [Submit]
43. Verifikasi Submit diblokir (modal tetap terbuka)

### TC-GS-UOM-48: Submit langsung dengan Unit Name duplikat sebelum debounce selesai

44. Klik [Clear Field]
45. Ketik Unit Name `Liter`, Symbol `ltr`, lalu segera klik [Submit] (kurang dari 500 ms)
46. Verifikasi server menolak dengan error inline `Unit name already exists` pada Unit Name
47. Verifikasi modal tetap terbuka

### TC-GS-UOM-51: Symbol 11 karakter

48. Klik [Clear Field]
49. Ketik Symbol `abcdefghijk` (11 karakter)
50. Verifikasi field Symbol menerima karakter ke-11
51. Verifikasi error inline `Max. 10 characters` tampil saat melebihi

### TC-GS-UOM-52: Symbol berisi emoji

52. Klik [Clear Field]
53. Isi Unit Name `Emoji Sym {runId}-020`
54. Ketik Symbol `kg😀`
55. Verifikasi error inline `Symbol contains invalid characters` tampil saat mengetik
56. Klik [Submit]
57. Verifikasi Submit diblokir (modal tetap terbuka)

### Pengecekan tidak ada unit tercipta dan penutupan form

58. Verifikasi tidak ada record baru: daftar Measurement Client A lewat API tidak memuat unit 121 karakter, `Box 📦`, `Emoji Sym {runId}-020`, `KILOGRAM`, maupun `meter` sebagai unit tambahan, dan hanya satu unit bernama `Liter`
59. Klik `[✕]` untuk menutup form yang masih dirty
60. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
61. Klik [Leave] pada dialog `Unsaved Changes`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh validasi memakai satu pembukaan form (prinsip 3, 7, dan "halaman yang sama dipakai berulang" konvensi): validasi diblokir berurutan, field dikosongkan dengan `[Clear Field]` di antara kasus (pembersih S-09 untuk dua kasus berurutan dengan error inline identik, termasuk 46 lalu 47), dan pengecekan "tidak ada record" dilakukan sekali di langkah 58 lewat API karena tabel tertutup modal. Form ditutup di akhir spec (langkah 59 sampai 61).
- TC-GS-UOM-39 dan TC-GS-UOM-335 digabung di langkah 1 sampai 11 karena memakai aksi yang sama (klik [Submit] dengan kedua field kosong); `aria-required` diperiksa sebelum Submit (Langkah Uji 2 TC-GS-UOM-335), `aria-describedby` dan focus trap sesudahnya (Langkah Uji 3 dan 4).
- Langkah penghubung (aksi tanpa `Verifikasi`): `[Clear Field]` di langkah 12, 17, 24, 30, 37, 44, 48, dan 52; mengisi Symbol pengisi (`x`, `bx`) di langkah 21, 27, 34, dan 41 dan Unit Name pendamping di langkah 53 agar penyebab blokir hanya field yang diuji; menutup form dirty di langkah 59 dan 61 (langkah 60 memverifikasi dialog, S-08).
- Langkah 22, 28, 35, 42, dan 56 (klik [Submit]) serta Verifikasi blokirnya (langkah 23, 29, 36, 43, 57) memenuhi prinsip 7 (tiap validasi diakhiri submit yang diblokir). TC-GS-UOM-43, 44, 47, dan 52 hanya menyebut error inline di Langkah Uji; Expected Result "Submit tidak membuat record" di TC-GS-UOM-43, 44, dan 52 diasersi lewat Submit yang diblokir plus langkah 58.
- Spec memuat 61 langkah (melewati batas 35 langkah). Alasan: semua blok berada di satu kelas harness (validasi Create yang diblokir), memakai satu form yang dibuka sekali, dan tiap blok berdiri sendiri karena `[Clear Field]` mengembalikan form ke keadaan awal, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Berbeda dengan Brand, emoji pada Unit Name dan Symbol tidak difilter di level input: PRD memvalidasi dan menampilkan error inline `Unit name contains invalid characters` dan `Symbol contains invalid characters` (NC-14, TC-GS-UOM-44 dan 52); spec mengikuti Expected Result TC.
- Temuan untuk QA:
  - TC-GS-UOM-43 menulis "Unit Name 121 karakter" tanpa menyebut jenis karakter; spec memakai huruf biasa.
  - TC-GS-UOM-44 dan 52 tidak menyebut Symbol atau Unit Name pendamping saat Submit; spec memakai nilai pengisi supaya penyebab blokir hanya emoji (langkah 27, 53).
  - TC-GS-UOM-48 mengandalkan pengetikan dan klik dalam kurang dari 500 ms; stabilitas waktunya bergantung pada kecepatan eksekusi runner.
