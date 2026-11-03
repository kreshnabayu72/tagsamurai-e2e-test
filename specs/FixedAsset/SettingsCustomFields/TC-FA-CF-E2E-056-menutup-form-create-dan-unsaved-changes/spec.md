---
id: TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes
title: "Menutup Form Create dan Dialog Unsaved Changes: Cancel, Leave, Esc, Backdrop, dan Form Kembali Bersih"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-176
  - TC-FA-CF-177
  - TC-FA-CF-178
  - TC-FA-CF-179
  - TC-FA-CF-180
  - TC-FA-CF-181
coverage:
  web: automated
---

# Menutup Form Create dan Dialog Unsaved Changes: Cancel, Leave, Esc, Backdrop, dan Form Kembali Bersih

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-056`): Field Name yang diketik tetapi tidak pernah tersimpan: `Dirty Keep {runId}-056`, `Dirty Esc {runId}-056`, `Dirty Bd {runId}-056`, dan `Dirty {runId}-056`; nilai sementara `X` (dihapus kembali). Tidak ada field yang tersimpan oleh spec ini.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-056`.
- Kemampuan teknis: penekanan tombol `Esc`; klik area backdrop di luar modal; pembacaan isi input Field Name.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-176: Menutup modal Create yang belum disentuh tidak menampilkan dialog Unsaved Changes

1. Klik [+ Custom Field]
2. Klik icon close `[✕]`
3. Verifikasi modal langsung tertutup tanpa dialog

### TC-FA-CF-181: Form yang diisi lalu dikembalikan identik dengan kondisi awal dianggap clean

4. Klik [+ Custom Field]
5. Ketik `X` pada Field Name lalu hapus kembali sampai kosong
6. Klik icon close `[✕]`
7. Verifikasi modal langsung tertutup tanpa dialog `Unsaved Changes`

### TC-FA-CF-178: Cancel pada dialog Unsaved Changes mempertahankan modal dan input

8. Klik [+ Custom Field]
9. Isi Field Name `Dirty Keep {runId}-056`
10. Tekan `Esc`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Cancel]` pada dialog
13. Verifikasi dialog tertutup
14. Verifikasi modal tetap terbuka
15. Verifikasi Field Name masih `Dirty Keep {runId}-056`

### TC-FA-CF-179: Esc pada dialog Unsaved Changes setara Cancel

16. Ganti isi Field Name dengan `Dirty Esc {runId}-056`
17. Klik icon close `[✕]`
18. Verifikasi dialog `Unsaved Changes` tampil
19. Tekan `Esc` saat dialog tampil
20. Verifikasi dialog tertutup
21. Verifikasi modal Create tetap terbuka
22. Verifikasi input dipertahankan: Field Name `Dirty Esc {runId}-056`

### TC-FA-CF-180: Klik backdrop modal Create yang terisi tidak menutup modal dan tidak memunculkan dialog

23. Ganti isi Field Name dengan `Dirty Bd {runId}-056`
24. Klik area backdrop di luar modal
25. Verifikasi modal tetap terbuka
26. Verifikasi input dipertahankan: Field Name `Dirty Bd {runId}-056`
27. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-FA-CF-177: Menutup modal Create yang terisi menampilkan dialog Unsaved Changes dan Leave menutup modal

28. Ganti isi Field Name dengan `Dirty {runId}-056`
29. Klik icon close `[✕]`
30. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
31. Klik `[Leave]`
32. Verifikasi dialog tertutup
33. Verifikasi modal tertutup

### Penutup: field yang diketik tidak tersimpan

34. Ketik Search `{runId}-056`, tekan Enter
35. Verifikasi empty state "No results found" tampil (field bersuffix `{runId}-056` tidak tersimpan)
36. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 176, 181, 178, 179, 180, 177 (urutan sumber 176 sampai 181). Kasus yang menutup modal bersih (176 dan 181) lebih dulu; empat kasus berikutnya memakai satu modal yang sama dan Field Name diganti (langkah 16, 23, 28) alih-alih membuka modal baru, karena kasus itu hanya mengetik tanpa Submit (bagian 3 prinsip 13, halaman yang sama dipakai berulang). Kasus penutupan dengan `[Leave]` (TC-FA-CF-177) ditaruh paling akhir karena menutup modal (S-10). Jumlah buka form (3) sama dengan kejadian menutup (langkah 2, 6, 29 sampai 33).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 4, 8, 34, 36, serta pengisian form dan klik tombol sebagai bagian langkah TC. Langkah 16, 23, dan 28 mengganti isi Field Name pada modal yang sama (menggantikan langkah "Klik [+ Custom Field]" dan "Isi Field Name" TC-FA-CF-179, 180, dan 177).
- Langkah 11 adalah Expected a TC-FA-CF-178 (dialog tampil). Langkah 18 (dialog tampil sebelum `Esc`) bukan Expected TC-FA-CF-179 dan ditambahkan sebagai anchor S-08. Langkah 25 adalah anchor positif bagi asersi absence dialog pada langkah 27 (bagian 8b butir 2).
- Langkah 34 sampai 36 memakai empty state hasil Search sebagai anchor positif (bagian 8b butir 2) bahwa "tanpa menyimpan field" pada TC-FA-CF-177 terpenuhi.
- Spec berada di sekitar batas 35 langkah (36 langkah): enam TC satu topik (menutup form Create) dengan satu dataset tanpa penyimpanan data.
- Temuan untuk QA:
  - TC-FA-CF-179: Expected tidak menyebut dialog `Unsaved Changes` tampil sebelum `Esc`; spec menambah `Verifikasi` dialog tampil (langkah 18) sebagai anchor.
  - TC-FA-CF-180: Langkah Uji tidak menyebut cara mengklik backdrop; spec mengklik area di luar modal.
  - Nama field memakai suffix `{runId}-056` (S-12) sehingga tidak sama dengan `Dirty`, `Dirty Keep`, `Dirty Esc`, dan `Dirty Bd` pada Data Uji TC.
