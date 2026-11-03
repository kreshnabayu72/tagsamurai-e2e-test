---
id: TC-AC-DN-E2E-050-create-toast-baris-baru-dan-klik-ganda
title: "Create Device Name: Toast 4 Detik, Baris Baru pada List, dan Klik Ganda Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-82
  - TC-AC-DN-83
  - TC-AC-DN-111
coverage:
  web: automated
---

# Create Device Name: Toast 4 Detik, Baris Baru pada List, dan Klik Ganda Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`); #16 Device Name inti `Barcode Station` (pembanding urutan A-Z pada TC-AC-DN-83); List dalam urutan default A-Z halaman pertama.
- Data Dinamis (dibuat lewat form Create): `Mobile Antenna {runId}-050`, `Antena Gedung Utara {runId}-050`, dan `Double Click Gateway {runId}-050`, semuanya `Unit` dan `Antenna`. Hook `after` menghapus ketiga record lewat fixture BE (kemampuan hapus record Device Name disediakan tim FE/BE; pembersihan tidak berasumsi setup berhasil penuh).
- Kemampuan teknis: menanam penanda pada dokumen halaman sebelum aksi dan membacanya sesudahnya untuk membuktikan halaman tidak dimuat ulang (TC-AC-DN-83); klik ganda cepat dengan selang kurang dari 200 ms (TC-AC-DN-111); disediakan tim FE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-82: Toast sukses muncul di kanan bawah dan hilang sendiri setelah 4 detik

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `Mobile Antenna {runId}-050` pada field Device Name
3. Klik field Measurement lalu pilih `Unit`
4. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
5. Klik `[Submit]`
6. Verifikasi toast berada di kanan bawah layar
7. Verifikasi toast sukses: "Success, device name has been created."
8. Amati toast selama 5 detik tanpa interaksi
9. Verifikasi toast sukses hilang sendiri setelah 4 detik

### TC-AC-DN-83: Device Name baru langsung muncul pada urutan A-Z tanpa refresh halaman

10. Klik tombol `+ Device Name` pada toolbar
11. Ketik `Antena Gedung Utara {runId}-050` pada field Device Name
12. Klik field Measurement lalu pilih `Unit`
13. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
14. Tanam penanda pada dokumen halaman
15. Klik `[Submit]`
16. Verifikasi List halaman pertama menampilkan `Antena Gedung Utara {runId}-050` pada posisi sebelum `Barcode Station` (urutan A-Z tanpa membedakan huruf besar atau kecil)
17. Verifikasi halaman tidak dimuat ulang (penanda halaman pada langkah 14 masih ada)

### TC-AC-DN-111: Klik ganda cepat pada Submit hanya membuat satu Device Name

18. Klik tombol `+ Device Name` pada toolbar
19. Ketik `Double Click Gateway {runId}-050` pada field Device Name
20. Klik field Measurement lalu pilih `Unit`
21. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
22. Klik `[Submit]` dua kali dengan cepat (selang kurang dari 200 ms)
23. Verifikasi tombol `[Submit]` berstatus disabled sejak klik pertama
24. Verifikasi satu toast sukses: "Success, device name has been created." tampil
25. Ketik Search `Double Click Gateway {runId}-050`, tekan Enter
26. Verifikasi List memuat tepat satu baris `Double Click Gateway {runId}-050`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Ketiga TC bertanda FE Test "Need API".
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 8 (menunggu toast selama 5 detik tanpa interaksi sesuai TC), langkah 14 (menanam penanda halaman), dan langkah 25 (Search untuk menemukan baris target, R-16).
- Langkah 23 diasersi segera sesudah klik ganda (state sementara, bagian 8b butir 5) dan sebelum asersi toast.
- Asersi tambahan (S-03): langkah 25 dan 26 membuktikan Expected c TC-AC-DN-111 ("tepat satu baris") pada List; langkah 17 memakai penanda halaman sebagai cara mengamati "halaman tidak dimuat ulang".
- Pencatatan satu set entri log Create (Post Condition TC-AC-DN-111 b) dicakup spec pencatatan log modul ini; spec ini tidak mengasersinya (S-05).
- Temuan untuk QA:
  - TC-AC-DN-83 Expected b ("Halaman tidak dimuat ulang") tidak menyebut cara pengamatan; spec memakai penanda halaman yang disediakan tim FE.
  - TC-AC-DN-83 menyebut posisi "sebelum `Barcode Station`" pada halaman pertama; hasil bergantung pada nama record lain yang berawalan huruf A pada List.
  - Post Condition TC-AC-DN-111 a ("Hanya satu record tersimpan") dan b tidak punya langkah observasi selain List, sehingga hanya List yang diasersi.
