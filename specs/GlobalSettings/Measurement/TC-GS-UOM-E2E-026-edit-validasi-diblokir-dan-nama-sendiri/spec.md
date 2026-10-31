---
id: TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri
title: "Validasi Edit yang Diblokir dan Nama Milik Sendiri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-76
  - TC-GS-UOM-77
  - TC-GS-UOM-78
  - TC-GS-UOM-80
  - TC-GS-UOM-81
  - TC-GS-UOM-82
  - TC-GS-UOM-263
  - TC-GS-UOM-336
coverage:
  web: automated
---

# Validasi Edit yang Diblokir dan Nama Milik Sendiri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession). Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: mengikuti pernyataan hook suite di `suite.md` (bagian Hook suite).
- Data pre-setup Client A (data baca): unit `Meter` / `m` hanya dibaca sebagai nama pembanding duplikat (TC-GS-UOM-77 mengetik `meter`); tidak diubah. Fixture belum ada; tim FE menyiapkan `fixtures/measurement.json` dengan kunci `preSetupClientA`.
- Data dinamis (seeding lewat API di hook `before`; tidak menumpang spec lain): `Edit Val {runId}-026` dengan Symbol `ev26` (bebas relasi), menggantikan `Sheet` dan `Liter` pada TC sumber agar baris Pre-setup tidak termutasi (S-06). Semua kasus diblokir sehingga unit ini tidak pernah tersimpan berubah.
- Nilai uji: string Unit Name 121 karakter dibangun helper (panjang total tepat 121 karakter, termasuk akhiran ` {runId}-026`, S-12); Symbol 11 karakter `abcdefghijk`; emoji Unit Name `Edit Val {runId}-026 💧`; emoji Symbol `L😀`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API unit `Edit Val {runId}-026`.
- Kemampuan teknis: pembacaan atribut `aria-required` dan `aria-describedby` pada field; penekanan Tab; pembacaan fokus elemen.
- State global: tidak ada yang diubah.

## Test Steps

### Persiapan

1. Ketik Search `Edit Val {runId}-026`, tekan Enter
2. Verifikasi baris `Edit Val {runId}-026` tampil di tabel

### TC-GS-UOM-78 dan TC-GS-UOM-336: Save Edit dengan field kosong dan aksesibilitas field

3. Klik `⋯` baris `Edit Val {runId}-026` > Edit
4. Hapus isi Unit Name dan Symbol
5. Klik [Save]
6. Verifikasi error `Unit name must not be empty`
7. Verifikasi error `Symbol must not be empty`
8. Verifikasi field Unit Name memiliki `aria-required="true"`
9. Verifikasi field Symbol memiliki `aria-required="true"`
10. Verifikasi field Unit Name memiliki `aria-describedby` yang menunjuk elemen pesan error miliknya
11. Verifikasi field Symbol memiliki `aria-describedby` yang menunjuk elemen pesan error miliknya
12. Tekan Tab berulang melewati elemen terakhir
13. Verifikasi fokus Tab berputar hanya di dalam popup
14. Verifikasi fokus tidak keluar ke halaman di belakang

### TC-GS-UOM-76: Mengetik ulang Unit Name milik sendiri

15. Ketik Unit Name `Edit Val {runId}-026`, tunggu debounce
16. Verifikasi tidak ada error `Unit name already exists`
17. Ketik Symbol `ev26`

### TC-GS-UOM-77: Edit Unit Name menjadi nama unit lain

18. Ganti isi Unit Name dengan `meter`, tunggu debounce
19. Verifikasi error inline `Unit name already exists`
20. Klik [Save]
21. Verifikasi Save ditolak: modal Edit tetap terbuka

### TC-GS-UOM-80: Edit Unit Name 121 karakter

22. Ganti isi Unit Name dengan string 121 karakter
23. Verifikasi input menerima karakter ke-121 (field berisi 121 karakter)
24. Verifikasi error inline `Max. 120 characters`

### TC-GS-UOM-81: Edit Unit Name berisi emoji

25. Ganti isi Unit Name dengan `Edit Val {runId}-026 💧`
26. Verifikasi error `Unit name contains invalid characters`

### TC-GS-UOM-82: Edit Symbol 11 karakter

27. Ganti isi Unit Name dengan `Edit Val {runId}-026`, tunggu debounce
28. Ganti isi Symbol dengan `abcdefghijk`
29. Verifikasi input menerima karakter ke-11 (field berisi 11 karakter)
30. Verifikasi error inline `Max. 10 characters`

### TC-GS-UOM-263: Edit Symbol berisi emoji

31. Ganti isi Symbol dengan `L😀`
32. Verifikasi error inline `Symbol contains invalid characters` muncul saat mengetik
33. Klik [Save]
34. Verifikasi modal Edit tetap terbuka (Save tidak menyimpan)

### Tutup form

35. Klik `[✕]`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik [Leave]
38. Verifikasi baris `Edit Val {runId}-026` tetap menampilkan Symbol `ev26`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Jumlah langkah: 38.
- Urutan TC dalam spec: 78/336, 76, 77, 80, 81, 82, 263 (urutan sumber 76, 77, 78, 80, 81, 82, 263, 336). TC-GS-UOM-78 dan TC-GS-UOM-336 berbagi langkah yang sama (mengosongkan kedua field lalu `[Save]`) sehingga digabung di awal; kasus berikutnya melanjutkan form yang sama dan tidak ada yang berhasil menyimpan (prinsip 7: tiap validasi berakhir pada submit yang diblokir atau tidak menyimpan). Kasus menutup form ada di akhir (prinsip 6): satu pembukaan form, satu kejadian menutup.
- Spec ini sekitar 38 langkah (di atas batas 35 langkah); alasan pertahanan: seluruhnya satu kelas (validasi diblokir pada satu form Edit milik spec), satu pembukaan form, dan tidak ada blok yang menciptakan atau menghapus data, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target), langkah 17 (mengisi Symbol `ev26` sehingga `[Save]` pada TC-GS-UOM-77 diblokir karena duplikat, bukan karena Symbol kosong), langkah 27 (mengembalikan Unit Name yang valid agar error Unit Name TC-81 tidak ikut tampil pada TC-82), dan langkah 35 sampai 37 (menutup form dirty lewat `[✕]` dan `[Leave]`, S-08).
- Langkah 2 adalah `Verifikasi` pembanding (butir 2 bagian 8b), bukan dari Expected TC.
- TC-GS-UOM-76 memakai nilai milik sendiri `Edit Val {runId}-026` (TC sumber: `Sheet`). Langkah "hapus lalu ketik ulang" TC sumber dipenuhi oleh langkah 4 (field dikosongkan) dan langkah 15 (diketik ulang).
- TC-GS-UOM-77 mengetik `meter` (huruf kecil) sesuai TC sumber; `Meter` Pre-setup menjadi pembanding duplikat tanpa diubah.
- TC-GS-UOM-263 butir b ("Symbol Liter tetap `L`") diasersi di langkah 38 dengan nilai milik spec (`ev26`).
- Temuan untuk QA:
  - TC-GS-UOM-80 Expected butir a ("Input menerima karakter ke-121") dan butir b (error `Max. 120 characters`) dipertahankan sesuai TC; butir a sejalan dengan PRD §9.9 V-01b (input tetap menerima karakter berlebih; Submit diblokir).
  - TC-GS-UOM-336 langkah 2 menekan `[Save]` dengan kedua field kosong; TC tidak menyatakan apakah request ke server terkirim. Spec hanya mengasersi error inline dan atribut aksesibilitas.
