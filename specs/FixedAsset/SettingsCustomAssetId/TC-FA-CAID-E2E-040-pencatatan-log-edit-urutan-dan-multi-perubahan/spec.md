---
id: TC-FA-CAID-E2E-040-pencatatan-log-edit-urutan-dan-multi-perubahan
title: "Pencatatan Log Edit: Segments Order, Multi Perubahan, dan Satu Entri per Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-243
  - TC-FA-CAID-244
  - TC-FA-CAID-245
coverage:
  web: automated
---

# Pencatatan Log Edit: Segments Order, Multi Perubahan, dan Satu Entri per Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup: Company Alpha dengan baseline B1 (No 10); baseline B1 disiapkan ulang lewat seed API pada langkah pertama tiap TC. General Settings Date Format `dd/MM/yy` dan Time Format 24 jam (No 27): dipakai sebagai precondition TC, tidak diasersi.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: konfigurasi Company Alpha berubah di tiap TC. Hook `after` suite memulihkan Company Alpha ke baseline B1 dan aset A1 sampai A5. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-243: Log Edit perubahan urutan segmen memakai (Segments Order)

1. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
2. Seret baris `Initial Company` ke posisi tepat di atas baris `Asset Increment`
3. Klik `[Save]`
4. Tunggu aksi selesai: tombol `[Save]` kembali disabled
5. Buka Modal Changelog: Custom Asset ID
6. Verifikasi satu baris baru dibanding baseline Action `Edit`, Field `Segments Formula`, Old Value `—`, New Value `(Segments Order) Initial Company, Group Code, Category Code, Asset Name Code, Division Code, Account Code, Purchase Date, Asset Increment ➔ Group Code, Category Code, Asset Name Code, Division Code, Account Code, Purchase Date, Initial Company, Asset Increment` tampil di Changelog
7. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
8. Verifikasi satu baris baru yang sama tampil di System Log
9. Buka Fixed Asset > Activity Log > tab User Action
10. Verifikasi satu baris baru yang sama tampil di Activity Log
11. Verifikasi kolom Old Value baris ini berisi `—` dan seluruh delta berada di New Value, sama di ketiga surface

### TC-FA-CAID-244: Satu Save dengan beberapa perubahan

12. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
13. Pilih Separator `- (Dash)`
14. Centang `Division Code` dan `Account Code`
15. Seret baris `Purchase Date (MMYY)` ke posisi paling atas
16. Klik `[Save]`
17. Tunggu aksi selesai: tombol `[Save]` kembali disabled
18. Buka Modal Changelog: Custom Asset ID
19. Verifikasi Changelog bertambah tepat dua baris baru dibanding baseline
20. Verifikasi satu baris baru Action `Edit`, Field `Separator`, Old Value `Slash`, New Value `Dash`
21. Verifikasi satu baris baru Action `Edit`, Field `Segments Formula`, New Value `(Division Code) Inactive ➔ Active; (Account Code) Inactive ➔ Active; (Segments Order) Initial Company, Group Code, Category Code, Asset Name Code, Division Code, Account Code, Purchase Date, Asset Increment ➔ Purchase Date, Initial Company, Group Code, Category Code, Asset Name Code, Division Code, Account Code, Asset Increment`
22. Verifikasi delta segmen pada New Value baris Segments Formula berurutan mengikuti formula baru dan `(Segments Order)` paling akhir
23. Verifikasi Old Value baris Segments Formula berisi `—`
24. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
25. Verifikasi System Log memuat dua baris baru yang sama dengan nilai identik dengan Changelog
26. Buka Fixed Asset > Activity Log > tab User Action
27. Verifikasi Activity Log memuat dua baris baru yang sama dengan nilai identik dengan Changelog

### TC-FA-CAID-245: Satu aksi mutasi menghasilkan tepat satu entri per field yang berubah

28. Atur konfigurasi Company Alpha ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat jumlah entri Object `Custom Asset ID` pada ketiga surface sebagai baseline
29. Pilih Separator `. (Dot)`
30. Klik `[Save]`
31. Tunggu aksi selesai: tombol `[Save]` kembali disabled
32. Buka Modal Changelog: Custom Asset ID
33. Verifikasi Changelog bertambah tepat satu entri dibanding baseline (Edit Separator `Slash` ke `Dot`)
34. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
35. Verifikasi System Log bertambah tepat satu entri dibanding baseline (Edit Separator `Slash` ke `Dot`)
36. Buka Fixed Asset > Activity Log > tab User Action
37. Verifikasi Activity Log bertambah tepat satu entri dibanding baseline (Edit Separator `Slash` ke `Dot`)
38. Verifikasi tidak ada entri ganda atau entri untuk field yang tidak berubah pada ketiga surface

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 38 langkah, di atas smell 35 langkah. Alasan: seluruhnya satu topik dan satu kelas harness (pencatatan log Edit) dengan tiga blok TC yang berpola sama; blok baca-log berpola (buka surface, lalu `Verifikasi` kolom log) tidak dihitung menurut bagian 3 prinsip 13, sehingga langkah di luar blok itu hanya 14 (langkah 1 sampai 4, 12 sampai 17, dan 28 sampai 31).
- Langkah penghubung: langkah 1, 12, dan 28 (seed baseline, membuka halaman, dan baseline jumlah entri, S-12), langkah 4, 17, dan 31 (tunggu aksi selesai sebelum membuka Modal Changelog, bagian 8b butir 8), serta membuka Modal Changelog, System Log, dan Activity Log.
- Langkah 38 menyimpulkan Expected "tidak ada entri ganda atau entri untuk field yang tidak berubah" dari jumlah entri yang sudah diasersi per surface pada langkah 33, 35, dan 37 (anchor positif); TC-FA-CAID-245 bukan kelas g karena berupa asersi jumlah.
- Format baris Edit Segments Formula (Old Value `—` dan seluruh delta di New Value, dipisah `; `) mengikuti keputusan NC-18 yang tercantum di TC.
- Pembagian TC lintas spec: TC-FA-CAID-233 sampai 235 ada di spec 037, TC-FA-CAID-236 sampai 238 di spec 038, TC-FA-CAID-239 sampai 242 di spec 039.
- Temuan untuk QA:
  - TC-FA-CAID-244 Expected a tidak menyebut Old/New untuk baris Segments Formula secara lengkap pada langkah a; spec mengasersi Old Value pada Expected c.
  - TC-FA-CAID-245 mencatat jumlah entri pada ketiga surface sebagai langkah pertama TC; baris ini dipakai sebagai baseline spec.
  - Post Condition TC-FA-CAID-243 sampai 245 tidak diasersi karena TC tidak memberi langkah observasinya.
