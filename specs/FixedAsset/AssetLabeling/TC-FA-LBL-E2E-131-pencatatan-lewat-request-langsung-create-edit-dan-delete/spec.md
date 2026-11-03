---
id: TC-FA-LBL-E2E-131-pencatatan-lewat-request-langsung-create-edit-dan-delete
title: "Pencatatan Lewat Request Langsung: Create, Edit, dan Delete"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-409
  - TC-FA-LBL-494
  - TC-FA-LBL-495
coverage:
  web: automated
---

# Pencatatan Lewat Request Langsung: Create, Edit, dan Delete

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (nama bersuffix `{runId}-131`):
  - `Api Log 409 {runId}-131` (TC-FA-LBL-409; dibuat oleh permintaan langsung, tanpa seed)
  - `Api Edit 494 {runId}-131` (TC-FA-LBL-494; label seed milik spec, Color `Fixture.assetLabeling.warnaSeed`, dibuat lewat fixture BE di hook `before`); nama sesudah perubahan `Api Edit 494 Baru {runId}-131`
  - `Api Delete 495 {runId}-131` (TC-FA-LBL-495; label bersih milik spec, Total Asset 0, bukan Default Label, dibuat lewat fixture BE di hook `before`)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: klien HTTP dengan token aktor Sarah Johnson (sesi API aktor, token tidak dihitung sebagai sesi web; dinyatakan di `suite.md`) untuk permintaan langsung ke server; fixture BE untuk seeding dan membersihkan label serta membaca jumlah dan isi entri Changelog Labels, System Log aktor, dan Activity Log (disediakan tim FE/BE; endpoint tidak ditulis di TC; S-12). Surface log dibaca lewat UI pada Modal Changelog: Labels, Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log, dan Fixed Asset > Activity Log; entri dicari berdasarkan nama label bersuffix unik (baseline nol). Kontrol pencarian pada System Log dan Activity Log disediakan tim FE (lihat Temuan untuk QA).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-131`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-409: Create lewat permintaan API langsung tercatat di ketiga surface

1. Kirim permintaan Create Label langsung ke server (token aktor Sarah Johnson) dengan nama `Api Log 409 {runId}-131` hingga label tersimpan
2. Klik icon Changelog di Table Tools
3. Ketik Search `Api Log 409 {runId}-131` di toolbar Modal Changelog, tekan Enter
4. Verifikasi satu entri Create di Changelog: Label Name `Api Log 409 {runId}-131`, Field `Label Name`, Old Value `—`, New Value `Api Log 409 {runId}-131`, Modified By `Sarah J`
5. Klik `[✕]` pada Modal Changelog
6. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
7. Cari entri dengan Name `Api Log 409 {runId}-131` di System Log
8. Verifikasi satu entri Create di System Log: Name `Api Log 409 {runId}-131`, Field `Label Name`, Old Value `—`, New Value `Api Log 409 {runId}-131`
9. Buka Fixed Asset > Activity Log
10. Cari entri dengan Name `Api Log 409 {runId}-131` di Activity Log
11. Verifikasi satu entri Create di Activity Log: Name `Api Log 409 {runId}-131`, Field `Label Name`, Old Value `—`, New Value `Api Log 409 {runId}-131`, Modified By `Sarah J`

### TC-FA-LBL-494: Edit lewat permintaan API langsung tercatat di ketiga surface log

12. Buka Fixed Asset > Settings > Asset Master > tab Labels
13. Kirim permintaan Edit langsung ke server (token aktor Sarah Johnson): nama `Api Edit 494 {runId}-131` menjadi `Api Edit 494 Baru {runId}-131` hingga perubahan tersimpan
14. Klik icon Changelog di Table Tools
15. Ketik Search `Api Edit 494 Baru {runId}-131` di toolbar Modal Changelog, tekan Enter
16. Verifikasi satu entri Edit di Changelog: Field `Label Name`, Old Value `Api Edit 494 {runId}-131`, New Value `Api Edit 494 Baru {runId}-131`
17. Verifikasi Modified By entri Changelog adalah `Sarah J` dan entri sama bentuknya dengan entri jalur form
18. Klik `[✕]` pada Modal Changelog
19. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
20. Cari entri dengan Name `Api Edit 494 Baru {runId}-131` di System Log
21. Verifikasi satu entri Edit di System Log: Field `Label Name`, Old Value `Api Edit 494 {runId}-131`, New Value `Api Edit 494 Baru {runId}-131`
22. Buka Fixed Asset > Activity Log
23. Cari entri dengan Name `Api Edit 494 Baru {runId}-131` di Activity Log
24. Verifikasi satu entri Edit di Activity Log: Field `Label Name`, Old Value `Api Edit 494 {runId}-131`, New Value `Api Edit 494 Baru {runId}-131`, Modified By `Sarah J`

### TC-FA-LBL-495: Delete lewat permintaan API langsung tercatat di ketiga surface log

25. Buka Fixed Asset > Settings > Asset Master > tab Labels
26. Kirim permintaan Delete langsung ke server (token aktor Sarah Johnson) untuk `Api Delete 495 {runId}-131` hingga penghapusan tersimpan
27. Klik icon Changelog di Table Tools
28. Ketik Search `Api Delete 495 {runId}-131` di toolbar Modal Changelog, tekan Enter
29. Verifikasi satu entri Delete di Changelog: Field `Label Name`, Old Value `Api Delete 495 {runId}-131`, New Value `—`
30. Verifikasi Modified By entri Changelog adalah `Sarah J` dan entri sama bentuknya dengan entri jalur form
31. Klik `[✕]` pada Modal Changelog
32. Buka Fixed Asset > Settings > User > Detail pengguna aktor > Tab System Log
33. Cari entri dengan Name `Api Delete 495 {runId}-131` di System Log
34. Verifikasi satu entri Delete di System Log: Field `Label Name`, Old Value `Api Delete 495 {runId}-131`, New Value `—`
35. Buka Fixed Asset > Activity Log
36. Cari entri dengan Name `Api Delete 495 {runId}-131` di Activity Log
37. Verifikasi satu entri Delete di Activity Log: Field `Label Name`, Old Value `Api Delete 495 {runId}-131`, New Value `—`, Modified By `Sarah J`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 5 (Pencatatan Audit Log & Multi-Surface Sync). Subjudul `###` memetakan langkah ke TC granular.
- K-1: TC-FA-LBL-409, 494, dan 495 adalah TC kelas a (defense-in-depth, permintaan langsung ke server) dengan Expected berupa entri log pada tiga surface. Spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Spec ini di atas smell (37 langkah) karena blok baca-log berpola (tiga surface per TC) dikecualikan menurut bagian 3 prinsip 13; selebihnya 8 langkah. Semua blok satu kelas (a) dan berdiri sendiri.
- Bagian 8b butir 1: langkah permintaan langsung hanya mengasersi state data lewat entri log pada UI; pengalihan halaman, toast, atau tampilan jalur form tidak diasersi. Permintaan dikirim tanpa asersi status karena TC tidak menyebut status respons.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target pada Labels List, Search pada Modal Changelog, pencarian entri Name pada System Log dan Activity Log, dan penutupan modal adalah langkah penghubung (nama bersuffix unik, baseline nol, S-12). Perpindahan ke System Log atau Activity Log mengosongkan Labels List sehingga langkah "Buka Fixed Asset > Settings > Asset Master > tab Labels" menyiapkan TC berikutnya.
- Langkah penghubung (S-03): pada TC-FA-LBL-494 dan 495 permintaan Edit dan Delete memakai sesi API aktor sehingga tidak ada langkah "Tunggu aksi selesai"; frasa "hingga ... tersimpan" menyatakan tunggu itu (R-20).
- Asersi "tidak ada entri log" untuk aksi yang ditolak, gagal, atau zero-delta ada di spec absence log nomor 132, 133, 134, dan 173 dengan aksi dan baseline masing-masing (S-05).
- Temuan untuk QA:
  - TC-FA-LBL-409, 494, dan 495 tidak menyebut status respons; spec tidak menambah asersi status (S-02). Expected b TC-FA-LBL-494 dan 495 ("entri sama dengan jalur form") ditulis sebagai kesamaan bentuk kolom entri dengan entri jalur form di spec 127 dan spec 129 (Edit nama dan Delete).
  - Cara mencari entri pada System Log dan Activity Log (Search atau Filter) tidak dijelaskan di TC; spec memakai nama label bersuffix unik dan kontrol pencarian yang tersedia di surface itu (disediakan tim FE).
