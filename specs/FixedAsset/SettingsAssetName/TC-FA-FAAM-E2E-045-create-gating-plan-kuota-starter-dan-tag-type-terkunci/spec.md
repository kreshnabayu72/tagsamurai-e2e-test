---
id: TC-FA-FAAM-E2E-045-create-gating-plan-kuota-starter-dan-tag-type-terkunci
title: "Create: Gating Plan (TAG Type Terkunci Starter, Paid, Paket Diturunkan) dan Satu di Bawah Kuota"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-110
  - TC-FA-FAAM-111
  - TC-FA-FAAM-113
  - TC-FA-FAAM-155
coverage:
  web: automated
---

# Create: Gating Plan (TAG Type Terkunci Starter, Paid, Paket Diturunkan) dan Satu di Bawah Kuota

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client Starter `AutoStarter` tanpa subscription Paid (Pre-setup #16). Email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_STARTER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client utama, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_STARTER_PASSWORD`, `FA_STARTER9A_PASSWORD`, `FA_PAID113_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Akun aktor berikutnya (ganti akun eksplisit di langkah spec): Total Control client `AutoStarter9a` plan Starter berisi 9 Asset Name, kuota 10 (Pre-setup #16e, `Spectra.env.FA_STARTER9A_PASSWORD`); Total Control client `AutoPaid113` dengan subscription Paid aktif (Pre-setup #16h, `Spectra.env.FA_PAID113_PASSWORD`); terakhir Total Control client utama dengan subscription Paid (Pre-setup #10, `Spectra.env.FA_TC_PASSWORD`, akun default suite). Email akun client khusus tidak tertulis di Pre-setup TC (disediakan tim FE).
- State global: subscription Paid terakhir `AutoPaid113` diturunkan ke Starter oleh pelaku kedua lewat sesi API aktor (TC-FA-FAAM-113) dan dipulihkan ke Paid di hook `after` (H7); suite berjalan serial.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 155 {runId}-045` dan `Create Min Item 113 {runId}-045` (yang kedua tidak tersimpan).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Create Min Item 155 {runId}-045` di client `AutoStarter9a` (jumlah kembali 9); pulihkan subscription `AutoPaid113` ke Paid.

## Test Steps

### TC-FA-FAAM-110: Client tanpa subscription Paid melihat RFID, NFC, BLE, GPS terkunci (client AutoStarter)

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Buka dropdown TAG Type
3. Verifikasi Opsi `RFID`, `NFC`, `BLE`, `GPS` terkunci 🔒 dengan tooltip `Upgrade to unlock`
4. Verifikasi Opsi `QR` dan `Non-TAG` dapat dipilih
5. Tutup dropdown TAG Type lalu klik `[✕]` (form bersih tertutup tanpa dialog)

### TC-FA-FAAM-155: Create saat jumlah Asset Name satu di bawah kuota paket berhasil (client AutoStarter9a)

6. Ganti akun: keluar (Logout), lalu login sebagai Total Control client `AutoStarter9a` (Pre-setup #16e; email disediakan tim FE, `Spectra.env.FA_STARTER9A_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
7. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
8. Isi field wajib: Asset Name `Create Min Item 155 {runId}-045`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
9. Klik `[Submit]`
10. Verifikasi Toast `Success, asset name has been created.` tampil
11. Verifikasi Jumlah Asset Name client menjadi 10 (total baris tabel)

### TC-FA-FAAM-113: Paket diturunkan saat form terbuka (client AutoPaid113)

12. Ganti akun: keluar (Logout), lalu login sebagai Total Control client `AutoPaid113` (Pre-setup #16h; email disediakan tim FE, `Spectra.env.FA_PAID113_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
13. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
14. Pilih TAG Type `RFID` dan `QR`
15. Turunkan subscription Paid terakhir `AutoPaid113` ke Starter lewat sesi API aktor kedua hingga perubahan paket tersimpan
16. Isi field wajib: Asset Name `Create Min Item 113 {runId}-045`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), Brand `Dell`, UoM `Unit`
17. Klik `[Submit]`
18. Verifikasi Error inline `This TAG type is not available on your plan.` tampil
19. Verifikasi Chip `RFID` dikosongkan
20. Verifikasi Chip `QR` bertahan
21. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

### TC-FA-FAAM-111: Client dengan subscription Paid dapat memilih semua tipe TAG (client utama)

22. Ganti akun: keluar (Logout), lalu login sebagai Total Control client utama (Pre-setup #10; email disediakan tim FE, `Spectra.env.FA_TC_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
23. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
24. Pilih TAG Type `RFID`, `NFC`, `BLE`, `GPS`
25. Verifikasi Keempat chip dapat dipilih tanpa kunci
26. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan TC dalam spec: client berganti tiga kali sehingga urutan mengikuti client (AutoStarter, AutoStarter9a, AutoPaid113, client utama) dan berakhir di akun default suite; TC-FA-FAAM-155 menambah satu record sehingga ditempatkan sebelum TC yang mengubah plan.
- Langkah "field wajib lain terisi" milik TC-FA-FAAM-113 diisi tanpa TAG Type karena `RFID` dan `QR` sudah dipilih pada langkah sebelumnya; subscription diturunkan sebelum `[Submit]`.
- Pelaku kedua lewat sesi API aktor (bukan konteks UI kedua), jadi `P-2` tidak dipakai; mekanisme penurunan subscription disediakan tim BE/FE tanpa endpoint karangan (S-13).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah pemulihan di akhir blok TC-FA-FAAM-113 dan TC-FA-FAAM-111) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-110, 113, 155 menyebut client khusus (Pre-setup #16, #16h, #16e) tanpa email dan nama env akun Total Control; nama env diusulkan `FA_STARTER_PASSWORD`, `FA_PAID113_PASSWORD`, `FA_STARTER9A_PASSWORD`.
  - TC-FA-FAAM-113 berlabel "Manual Only (d) dua sesi paralel"; spec memicu penurunan paket lewat sesi API aktor.
  - TC-FA-FAAM-155 Expected "jumlah menjadi 10" tidak menyebut surface jumlahnya; spec memakai total baris tabel.
