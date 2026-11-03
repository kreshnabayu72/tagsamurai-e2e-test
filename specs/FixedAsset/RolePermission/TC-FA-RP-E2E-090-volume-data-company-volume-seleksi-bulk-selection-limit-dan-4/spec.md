---
id: TC-FA-RP-E2E-090-volume-data-company-volume-seleksi-bulk-selection-limit-dan-4
title: "Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (4/4)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-943
  - TC-FA-RP-944
  - TC-FA-RP-971
coverage:
  web: automated
---

# Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (4/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`; pelaku request langsung kedua: Read Only Dewi Anggraini (Pre-setup #4), `readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`, lewat sesi API. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec ini tidak punya langkah UI; seluruh langkah memakai sesi API, sehingga tidak ada ganti akun UI.
- Environment variable: `FA_TC_PASSWORD`, `FA_RO_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Sesi API aktor: login API untuk pelaku kedua dan pembacaan state lewat fixture BE mengikuti pernyataan di suite.md.
- Data Pre-setup: pool #15 (enam user: Ahmad Fauzi, Budi Santoso, Budi Setiawan, Citra Lestari, Dimas Pranata, Endah Susanti; tanpa tingkat akses) dan #4 (Dewi Anggraini). Keenam user memegang Global Role `Manage Open API` untuk TC-FA-RP-944 (seed API di hook `before`). Selection Limit diturunkan ke 5 (Pre-setup #34); dicatat nilai awalnya di hook `before` dan dipulihkan di hook `after` walau spec gagal di tengah; state global ini membuat suite berjalan serial (`parallel: false`, lihat suite.md).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP untuk request langsung ke server dengan sesi API Total Control dan Read Only; pembacaan state data lewat fixture BE; penyetelan Selection Limit di System Limits.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan `Manage Open API` pool #15, daftar Total Control, dan Selection Limit), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-943: Assign melebihi Selection Limit ditolak server seluruhnya tanpa partial success

1. Kirim request langsung ke server (klien HTTP, sesi API Total Control, bukan lewat UI) untuk meng-Assign Total Control ke 6 user (Ahmad Fauzi, Budi Santoso, Budi Setiawan, Citra Lestari, Dimas Pranata, Endah Susanti) ketika Selection Limit diturunkan ke 5
2. Verifikasi respons status `422`
3. Periksa state lewat fixture BE: Verifikasi daftar Total Control memuat Siti Rahmawati (pembanding bahwa pembacaan state berhasil)
4. Verifikasi tidak ada satu pun penugasan Total Control dibuat untuk keenam user

### TC-FA-RP-944: Bulk Remove melebihi Selection Limit ditolak seluruhnya

5. Kirim request langsung ke server (klien HTTP, sesi API Total Control, bukan lewat UI) untuk Bulk Remove 6 baris pada `Manage Open API` ketika Selection Limit diturunkan ke 5
6. Verifikasi respons status `422`
7. Periksa state lewat fixture BE: Verifikasi keenam baris `Manage Open API` masih ada (tidak ada baris yang terhapus)

### TC-FA-RP-971: Urutan penolakan server: permission mendahului Selection Limit

8. Kirim request langsung ke server (klien HTTP, sesi API Read Only Dewi Anggraini, bukan lewat UI) untuk meng-Assign Total Control ke 6 user ketika Selection Limit diturunkan ke 5
9. Verifikasi respons status `403` dengan pesan `You don't have permission to do this.`
10. Verifikasi respons bukan penolakan Selection Limit: status `403`, bukan `422`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-943, TC-FA-RP-944, TC-FA-RP-971).
- K-1: TC-FA-RP-943, TC-FA-RP-944, dan TC-FA-RP-971 adalah TC kelas a (defense-in-depth) dengan Expected respons API; tetap masuk spec FE+BE walau tumpang tindih dengan TC backend karena TC granular tetap sumber dan tiap TC tepat satu spec; BE mencatatnya pada tingkat endpoint.
- Request langsung ke server (bagian 8b butir 1): asersi hanya respons server (status dan pesan) dan state data lewat fixture BE; tidak ada asersi UI.
- Penempatan di spec volume data (kelas e) karena Selection Limit diturunkan lewat Pre-setup #34; spec ini tidak punya langkah UI sehingga ganti akun UI tidak diperlukan.
- Temuan untuk QA:
  - TC-FA-RP-943 dan TC-FA-RP-944 mencantumkan Pre-setup #23 (Company Volume) sementara 6 user berasal dari pool #15 (Company Alpha); spec memakai pool #15 pada Company Alpha dan menyetel Selection Limit ke 5.
  - TC-FA-RP-971 tidak menyebut identitas 6 user dan tidak mengamati state data; hanya respons yang diasersi. "Penolakan Selection Limit tidak dipakai" diamati sebagai status `403` (bukan `422`).
  - TC-FA-RP-943 dan TC-FA-RP-944 tidak menyebut bentuk body respons selain status `422`; hanya status yang diasersi.
  - Pada TC-FA-RP-944 "tidak ada baris yang terhapus" memakai baris Pre-setup yang hanya diperiksa keberadaannya; tidak ada pembanding lain yang diperlukan (asersi positif atas keenam baris).
