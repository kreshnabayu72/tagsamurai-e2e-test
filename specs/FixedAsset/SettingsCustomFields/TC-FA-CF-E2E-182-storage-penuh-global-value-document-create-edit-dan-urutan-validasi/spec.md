---
id: TC-FA-CF-E2E-182-storage-penuh-global-value-document-create-edit-dan-urutan-validasi
title: "Global Value Document: Storage Penuh Menolak Create dan Edit Tanpa Mutasi, Format dan Ukuran Didahulukan"
priority: High
caseType: Negative
status: draft
sourceRules: ["FACF-LOGIC-12c", "VAL-FACF-36", "TOAST-FACF-17", "E-FACF-46", "E-FACF-47", "F-FACF-11.k8", "VAL-FACF-32", "VAL-FACF-33"]
trace:
  "FACF-LOGIC-12c": [12, 14, 17, 24, 27, 32, 33, 38, 41]
  "VAL-FACF-36": [12, 14, 17, 18, 32, 33]
  "TOAST-FACF-17": [14, 16, 32]
  "E-FACF-46": [14, 17, 18, 24, 27, 32, 33, 38, 41]
  "E-FACF-47": [5, 6, 8, 9]
  "F-FACF-11.k8": [14, 17, 24, 32, 38, 41]
  "VAL-FACF-32": 5
  "VAL-FACF-33": 8
coverage:
  web: automated
---

# Global Value Document: Storage Penuh Menolak Create dan Edit Tanpa Mutasi, Format dan Ukuran Didahulukan

## Prerequisites

- Mode: FE+BE (backend nyata; cek Storage dijalankan server berdasarkan usage ledger saat Submit atau Save dikomit).
- Sumber: spec ini diturunkan langsung dari PRD `fixed-asset/settings-custom-fields/PRD/settings-custom-fields.md` (aturan `FACF-LOGIC-12c`, `VAL-FACF-36`, `TOAST-FACF-17`, `E-FACF-46`, `E-FACF-47`, `F-FACF-11.k8`); belum ada TestCase untuk aturan ini sehingga `sourceTc` tidak ada dan `sourceRules` mengutip ID PRD (konvensi sumber PRD).
- Akun aktor: Total Control pada Company Storage Penuh `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` berisi nama Company Storage Penuh (Company baru dengan usage ledger Storage sama dengan atau di atas kuota; disediakan tim FE/BE; belum tercatat di Pre-setup). Password lewat `Spectra.env.FA_CFSTORAGE_TC_PASSWORD` (nama env baru yang diusulkan; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca; disediakan tim FE/BE lewat seed reset Company): Company Storage Penuh dengan nilai terpakai `{usedStorage}` dan kuota `{storageQuota}` (format Size File Manager, dibaca dari `Fixture.faCustomFields.storagePenuh`, fixture baru) dan satu field baseline `Global Doc Penuh` (Document, Scope General, Value Type Global, berkas `original.pdf`, tab General).
- Berkas uji (Pre-setup #36; fixture berkas `Fixture.berkasUji`): `valid.pdf`, `replacement.pdf`, `over-1mb.pdf` (1 MB lebih satu byte), `malware.exe`.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-182`): `Global Doc Baru {runId}-182` (Document, Global; tidak boleh tersimpan).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Storage Penuh yang namanya memuat `{runId}-182`; pulihkan `Global Doc Penuh` ke berkas `original.pdf` bila berubah.
- Kemampuan teknis: pemilihan berkas lewat file picker; injeksi berkas ke kontrol dengan melewati file picker (Pre-setup #26); membaca jumlah entri Modal Changelog tab General sebagai baseline (disediakan tim FE/BE; audit trail permanen).
- State global: tidak ada yang diubah; usage ledger Company Storage Penuh tetap karena tidak ada file yang berhasil disimpan. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Modal Changelog tab General, catat jumlah total entri sebagai baseline N0, lalu tutup Modal Changelog
2. Klik [+ Custom Field]

### E-FACF-47: Penolakan format dan ukuran didahulukan dari toast Storage penuh

3. Isi Field Name `Global Doc Baru {runId}-182`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
4. Injeksi berkas `malware.exe` ke kontrol (melewati file picker)
5. Verifikasi pesan inline "Unsupported file format. Use PDF, DOCX, DOC, XLS, XLSX, PNG, JPG, JPEG, or CSV." tampil pada kontrol
6. Verifikasi toast Storage penuh tidak tampil
7. Pilih berkas `over-1mb.pdf`
8. Verifikasi pesan inline "File size must not exceed 1 MB." tampil pada kontrol
9. Verifikasi toast Storage penuh tidak tampil

### E-FACF-46: Create dengan file Global Value baru saat Storage penuh ditolak tanpa mutasi

10. Pilih berkas `valid.pdf`
11. Verifikasi nama file `valid.pdf` tampil pada kontrol
12. Verifikasi toast Storage penuh tidak tampil saat file hanya dipilih (cek Storage dijalankan saat Submit)
13. Klik [Submit]
14. Verifikasi toast error persisten "Error, failed to upload document. Storage is full ({usedStorage} of {storageQuota} used)." tampil
15. Tunggu 10 detik tanpa menutup toast
16. Verifikasi toast error masih tampil
17. Verifikasi modal Create tetap terbuka
18. Verifikasi Field Name `Global Doc Baru {runId}-182` dan nama file `valid.pdf` tetap terisi
19. Tutup toast error secara manual
20. Klik `[✕]`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik `[Leave]`
23. Ketik Search `Global Doc Baru {runId}-182`, tekan Enter
24. Verifikasi tabel menampilkan `No results found`
25. Klik `(←)` pada kotak Search
26. Buka Modal Changelog tab General
27. Verifikasi jumlah total entri sama dengan baseline N0 (tidak ada entri Create)
28. Tutup Modal Changelog

### E-FACF-46: Edit dengan file pengganti baru saat Storage penuh ditolak dan file lama tidak dibuang

29. Klik row action `⋯` > `Edit` pada baris `Global Doc Penuh`
30. Pilih berkas `replacement.pdf`
31. Klik `[Save]`
32. Verifikasi toast error persisten "Error, failed to upload document. Storage is full ({usedStorage} of {storageQuota} used)." tampil
33. Verifikasi modal Edit tetap terbuka dengan nama file `replacement.pdf` tetap terpilih
34. Tutup toast error secara manual
35. Klik `[✕]`
36. Klik `[Leave]`
37. Klik row action `⋯` > `Edit` pada baris `Global Doc Penuh`
38. Verifikasi kontrol Value menampilkan nama file `original.pdf` pre-filled
39. Klik `[✕]`
40. Buka Modal Changelog tab General
41. Verifikasi jumlah total entri sama dengan baseline N0 (tidak ada entri Edit)
42. Tutup Modal Changelog

## Notes

- Spec di atas smell 35 langkah (42 langkah): tiga blok berbagi satu Company Storage Penuh dan satu baseline Changelog (N0 pada langkah 1) sehingga pembuktian "tanpa entri log" memakai satu pembanding.
- Sumber PRD, bukan TC (belum ada TestCase untuk `FACF-LOGIC-12`). Blok penolakan format dan ukuran (tanpa mutasi) berjalan lebih dulu karena modal Create yang sama dipakai blok sesudahnya.
- `VAL-FACF-36` mengharuskan cek Storage saat Save dikomit, bukan saat file dipilih: langkah 12 mengasersi tidak ada toast saat file hanya dipilih, toast baru tampil sesudah Submit (langkah 14).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline N0), langkah 2 (buka modal), langkah 19 sampai 22 dan 34 sampai 36 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` pada langkah 21 mengikuti S-08), langkah 25, 28, 39, dan 42 (membersihkan Search dan menutup modal).
- Nilai terpakai vs kuota pada toast adalah snapshot ledger saat cek dan bergantung pada seed Company Storage Penuh; kedua nilai dibaca dari fixture, bukan ditulis di spec.
- Sisi "client tanpa kuota Storage tidak diblokir" dari `E-FACF-47` tidak diotomasi di spec ini: butuh Client tanpa kuota Storage yang tidak tercatat di Pre-setup dan aturan dasarnya dimiliki `plans.md` §2.5b (lihat halaman coverage).
- Temuan untuk QA:
  - PRD tidak menyebut cara menutup toast `TOAST-FACF-17` selain persisten; langkah 19 dan 34 menutupnya manual lewat kontrol tutup toast.
