---
id: TC-AC-PP-E2E-051-log-absence-tanpa-pencatatan
title: "Aksi Tanpa Pencatatan: View, Search, Download, Publish Gagal, dan Versi Seed Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-158
  - TC-AC-PP-159
  - TC-AC-PP-160
coverage:
  web: automated
---

# Aksi Tanpa Pencatatan: View, Search, Download, Publish Gagal, dan Versi Seed Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk TC-AC-PP-159).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`, `Spectra.env.AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Hook `before`: Fixture BE men-seed Riwayat A (Version 3 Active, Version 2, Version 1). Log tidak dapat dihapus, sehingga spec memakai baseline jumlah entri. Hook `after` mengembalikan dataset ke Riwayat A.
- Dataset berganti di tengah spec lewat Fixture BE: Riwayat A untuk TC-AC-PP-158 dan TC-AC-PP-159, lalu Riwayat S (Version 1 `System` hasil seed, Version 2 `Budi`, Version 3 `Jane Smith` dengan akun sudah dihapus) untuk TC-AC-PP-160.
- Baseline log (S-12): sebelum tiap aksi, jumlah entri dengan Object `Privacy Policy` pada Activity Log (Admin Console) dan System Log `Andi Wijaya` (Settings > User > Detail `Andi Wijaya` > Tab System Log) dicatat; asersi memakai selisih terhadap baseline, bukan nilai absolut (log tidak dapat dihapus lewat UI). Untuk TC-AC-PP-160 baseline berupa jumlah entri `Publish` ber-Name `Version 1` (Object `Privacy Policy`) pada kedua surface, dicatat sebelum seed Riwayat S.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons Publish 500 dan mengganti body permintaan Publish dengan konten kosong (TC-AC-PP-159); Fixture BE; intercept dilepas segera setelah pemicu.
- Dokumen Privacy Policy bersifat tunggal platform-wide sehingga suite berjalan serial (`parallel: false`); spec ini tidak membuat versi baru yang tersimpan (semua Publish ditolak atau gagal).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec).
- Fixture `fixtures/privacyPolicy.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlHalamanPrivacyPolicy` | URL langsung Settings > Privacy Policy | Langkah 3, 12, 42 |

## Test Steps

### TC-AC-PP-158: View, Search, dan Download tidak menulis entri log

1. Buka Activity Log (Admin Console) dan catat jumlah entri dengan Object `Privacy Policy` sebagai baseline Activity Log
2. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log dan catat jumlah entri dengan Object `Privacy Policy` sebagai baseline System Log
3. Buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`)
4. Klik teks tautan `Version 3` sehingga Modal View terbuka, lalu tutup dengan `[✕]`
5. Klik icon Search, ketik "doe", lalu tekan Enter
6. Klik icon Download lalu pilih "Download as CSV"
7. Buka Activity Log dan hitung entri dengan Object `Privacy Policy`
8. Buka System Log `Andi Wijaya` dan hitung entri dengan Object `Privacy Policy`
9. Verifikasi jumlah entri dengan Object `Privacy Policy` pada Activity Log sama dengan baseline Activity Log
10. Verifikasi jumlah entri dengan Object `Privacy Policy` pada System Log `Andi Wijaya` sama dengan baseline System Log

### TC-AC-PP-159: Publish yang gagal atau ditolak tidak menulis entri log

11. Buka Activity Log dan catat jumlah entri dengan Object `Privacy Policy` sebagai baseline Activity Log
12. Buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`), klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
13. Klik di akhir konten editor lalu ketik " Absence check."
14. Atur intercept agar respons Publish menjadi server error 500
15. Klik `[Publish New Version]` lalu klik `[Publish]`
16. Lepas intercept respons Publish
17. Klik `[✕]`
18. Verifikasi Dialog "Unsaved Changes" tampil
19. Klik `[Leave]`
20. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
21. Klik `[Clear Field]` lalu klik `[Publish New Version]` sehingga Publish diblokir client oleh validasi V-01
22. Klik `[✕]`
23. Verifikasi Dialog "Unsaved Changes" tampil
24. Klik `[Leave]`
25. Klik `[⋯]` pada baris `Version 3` lalu pilih `Edit`, tunggu konten termuat
26. Klik di akhir konten editor lalu ketik " Absence check."
27. Klik `[Publish New Version]`
28. Atur intercept agar body permintaan Publish diganti dengan konten kosong (`""`)
29. Klik `[Publish]` sehingga server menolak permintaan (422)
30. Lepas intercept body permintaan Publish
31. Klik `[✕]`
32. Verifikasi Dialog "Unsaved Changes" tampil
33. Klik `[Leave]`
34. Buka Activity Log dan hitung entri dengan Object `Privacy Policy`
35. Verifikasi jumlah entri dengan Object `Privacy Policy` pada Activity Log sama dengan baseline Activity Log setelah ketiga kondisi (server error 500, blokir client V-01, penolakan server 422)

### TC-AC-PP-160: Versi 1 hasil seed tidak memiliki entri log

36. Catat baseline: buka Activity Log (Admin Console) dan Settings > User > Detail `Andi Wijaya` > Tab System Log, catat pada masing-masing surface jumlah entri `Publish` dengan Object `Privacy Policy` dan Name `Version 1`
37. Kembalikan dataset ke Riwayat S lewat Fixture BE
38. Buka Activity Log dan hitung entri `Publish` dengan Object `Privacy Policy` dan Name `Version 1`
39. Verifikasi tidak ada entri `Publish` untuk `Version 1` pada Activity Log: jumlahnya sama dengan baseline langkah 36
40. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log dan hitung entri `Publish` dengan Object `Privacy Policy` dan Name `Version 1`
41. Verifikasi tidak ada entri `Publish` untuk `Version 1` pada System Log: jumlahnya sama dengan baseline langkah 36
42. Buka Settings > Privacy Policy (`urlHalamanPrivacyPolicy`) dan amati baris `Version 1`
43. Verifikasi baris `Version 1` pada tabel Version History tetap menampilkan Published By `System`


## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Kelas harness g (asersi absence). Spec ini adalah rumah asersi absence untuk modul Privacy Policy; TC fungsional di spec lain yang memuat Post Condition "tidak ada record audit" mencatat rujukan ke spec ini.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung: langkah 4 (tutup Modal View), 16 dan 30 (lepas intercept), 17 sampai 19, 22 sampai 24, dan 31 sampai 33 (tutup modal Edit lewat `[✕]`, verifikasi dialog, `[Leave]`), 36 (catat baseline entri `Publish` `Version 1`), 37 (kembalikan dataset ke Riwayat S lewat Fixture BE), serta 38 dan 40 (langkah baca: hitung entri).
- S-08/S-03: langkah 18, 23, dan 32 memverifikasi Dialog "Unsaved Changes" sebelum `[Leave]` agar penutupan form dirty deterministik (S-08); verifikasi itu bukan Expected TC dan dicatat di sini sebagai asersi tambahan beralasan.
- P-2 (pemicu bukan objek uji): respons 500 (langkah 14) dan penggantian body Publish menjadi konten kosong (langkah 28) adalah kegagalan yang dipaksa hanya sebagai pemicu kondisi Publish gagal/ditolak; objek asersinya adalah jumlah entri log (kelas g), bukan perilaku kegagalan. Intercept dilepas segera setelah pemicu (langkah 16 dan 30).
- Ukuran spec: 43 langkah (melewati sekitar 35) karena tiap klausa Expected menjadi satu `Verifikasi` (S-01) dan tiap penutupan form memakai tiga langkah deterministik (S-08). Spec tidak dipecah: ketiga blok TC mandiri (dataset di-reseed di awal blok, baseline dicatat per blok), satu kelas harness (g), sehingga kegagalan satu blok tidak membuat blok berikutnya kehilangan makna.
- Asersi tambahan atas TC: langkah 9, 10, 35, 36, 39, 41 memakai baseline jumlah entri (S-12; blok TC-AC-PP-160 membandingkan jumlah entri `Publish` Name `Version 1` dengan baseline langkah 36 karena log append-only dan TC-AC-PP-35, 156, 188 juga menulis entri `Version 1`) karena log tidak bisa dibersihkan; baseline System Log dicatat di langkah 2 walau precondition TC hanya menyebut jumlah Activity Log, sebab langkah 4 TC menghitung kedua surface. Langkah 42 dan 43 adalah observasi Expected b TC-AC-PP-160 (tabel perlu dibuka karena TC tidak mencantumkan langkahnya).
- Temuan untuk QA:
  - TC-AC-PP-159 tidak menyebut isi teks yang diketik pada kondisi 500 dan 422; spec memakai " Absence check." agar konten berbeda dari Version 3 (bukan konten identik yang akan menjadi No-op).
  - TC-AC-PP-160 langkah 2 berbunyi "System Log aktor mana pun"; spec memakai System Log `Andi Wijaya` karena TC tidak menetapkan aktor.
  - Post Condition TC-AC-PP-158 sampai 160 ("tidak ada record audit baru") tidak punya langkah observasi di luar Expected dan tidak diasersi tambahan.
