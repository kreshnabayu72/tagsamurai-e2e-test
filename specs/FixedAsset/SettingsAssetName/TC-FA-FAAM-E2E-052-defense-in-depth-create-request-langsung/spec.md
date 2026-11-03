---
id: TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung
title: "Defense-in-Depth Create: Request Langsung Category Excess, Opsi Terkunci, Addon, dan Emoji"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-92
  - TC-FA-FAAM-105
  - TC-FA-FAAM-112
  - TC-FA-FAAM-120
  - TC-FA-FAAM-121
  - TC-FA-FAAM-137
coverage:
  web: automated
---

# Defense-in-Depth Create: Request Langsung Category Excess, Opsi Terkunci, Addon, dan Emoji

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`, `FA_STARTER_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Akun aktor kedua (ganti akun eksplisit di langkah spec, untuk TC-FA-FAAM-112): Total Control client Starter (Pre-setup #16), email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_STARTER_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Kemampuan teknis (disediakan tim BE/FE): klien HTTP yang mengirim request Create langsung ke server dengan token sesi API aktor (tidak melewati browser) dan payload valid selain bagian yang diuji; tanpa endpoint karangan (S-13). Pembacaan jumlah baris List sebagai baseline (S-12).
- Data Pre-setup (hanya dibaca): Category excess `Legacy Category` (Pre-setup #22d); lisensi addon `Maps` tidak teralokasi aktif (Pre-setup #10b); client Starter (Pre-setup #16). Asset Name `Create Min Item {runId}-052` hanya diketik dan tidak tersimpan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name apa pun yang ternyata terbentuk oleh request langsung (seharusnya tidak ada); tidak ada data lain yang dibuat.

## Test Steps

### TC-FA-FAAM-92: Emoji yang lolos filter FE ditolak dengan pesan fallback

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Injeksi value `Item 😊` langsung ke DOM field Asset Name (bypass keystroke filter FE)
3. Verifikasi Error inline `Asset name contains invalid characters` muncul real-time
4. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

### TC-FA-FAAM-137: Emoji pada model yang lolos filter FE ditolak server dengan error inline

5. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
6. Pilih Brand `Dell`
7. Isi field wajib: Asset Name `Create Min Item {runId}-052`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, UoM `Unit`
8. Injeksi model berisi emoji langsung ke input model (bypass filter FE)
9. Klik `[Submit]`
10. Verifikasi Error inline `Model name contains invalid characters` tampil pada input model
11. Verifikasi Record tidak dibuat: modal tetap terbuka tanpa toast `Success, asset name has been created.`
12. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

### TC-FA-FAAM-105, 120, 121: Request langsung ke server (client utama)

13. Catat jumlah baris List sebagai baseline
14. Kirim request Create langsung ke server dengan Category excess `Legacy Category`
15. Verifikasi Server menolak dengan `422` (error validasi pada Category)
16. Kirim request Create langsung dengan TAG Type `Non-TAG` dan Default Addon `Audit`
17. Verifikasi Server menolak request (karena Default Addon mensyaratkan TAG)
18. Kirim request Create langsung dengan Default Addon `Maps` saat lisensi Maps tidak aktif
19. Verifikasi Server menolak request (lisensi addon tidak aktif)
20. Muat ulang List
21. Verifikasi Jumlah baris List sama dengan baseline (tanpa mutasi)

### TC-FA-FAAM-112: Opsi TAG Type terkunci paket yang dikirim langsung ke server ditolak (client Starter)

22. Ganti akun: keluar (Logout), lalu login sebagai Total Control client Starter (Pre-setup #16; email disediakan tim FE, `Spectra.env.FA_STARTER_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
23. Catat jumlah baris List client Starter sebagai baseline
24. Kirim request Create langsung ke server dengan TAG Type `RFID` dari client Starter (Pre-setup #16)
25. Verifikasi Server menolak dengan `409 PLAN_LIMIT_EXCEEDED` dengan `reason: "feature_locked"`
26. Muat ulang List
27. Verifikasi Jumlah baris List sama dengan baseline (record tidak dibuat, tanpa mutasi)

## Notes

- K-1: TC-FA-FAAM-105, 112, 120, 121 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE karena TC granular tetap sumber (konvensi bagian 2).
- Request langsung hanya mengasersi respons server dan state data (bagian 8b butir 1). Pemeriksaan jumlah baris List untuk TC-FA-FAAM-105, 120, dan 121 dilakukan sekali sesudah ketiga request (langkah 21 terhadap baseline langkah 13) karena ketiganya ditolak tanpa mutasi dengan Expected state yang sama.
- Pembagian TC lintas spec: absence entri Changelog, System Log, dan Activity Log FAMS atas request Create langsung yang ditolak ada di spec 252 (TC-FA-FAAM-845).
- Langkah penghubung (tanpa `Verifikasi`): muat ulang List, pencatatan baseline, dan pemulihan form.
- Temuan untuk QA:
  - TC-FA-FAAM-120 dan 121 menulis "Server menolak" tanpa kode status; spec mengasersi penolakan tanpa kode tertentu. Perlu kode status pasti di TC.
  - TC-FA-FAAM-112 menyebut Client Starter (Pre-setup #16) tanpa email dan nama env akun; nama env diusulkan `FA_STARTER_PASSWORD`.
  - TC-FA-FAAM-92 dan 137 adalah injeksi DOM lewat UI (bukan request langsung ke server); keduanya dikelompokkan di spec kelas a bersama TC request langsung sesuai pengelompokan.
