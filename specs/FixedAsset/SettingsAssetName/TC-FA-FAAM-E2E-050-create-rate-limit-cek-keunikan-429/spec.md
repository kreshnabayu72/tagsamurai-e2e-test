---
id: TC-FA-FAAM-E2E-050-create-rate-limit-cek-keunikan-429
title: "Create: Cek Keunikan Ditolak Batas Laju (429) pada Asset Name, Code, dan Nama Model"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-683
  - TC-FA-FAAM-725
  - TC-FA-FAAM-726
coverage:
  web: automated
---

# Create: Cek Keunikan Ditolak Batas Laju (429) pada Asset Name, Code, dan Nama Model

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Kemampuan teknis: `Spectra.intercept()` memaksa respons endpoint pembacaan keunikan (Asset Name, Code, nama model) berstatus 429 hanya selama pengetikan; intercept dilepas segera sesudah tiap pemicu selesai (S-09). Tidak ada counter rate-limit nyata yang diubah, sehingga tidak ada state global yang perlu direset di hook `after`.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Rate Limit Item {runId}-050` (tersimpan di TC-FA-FAAM-683); Code `RATE-LIMIT` dan model `Rate Limit Model` hanya diketik dan tidak tersimpan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepaskan intercept bila masih aktif; hapus lewat API Asset Name `Rate Limit Item {runId}-050` bila masih ada.

## Test Steps

### TC-FA-FAAM-683: Cek keunikan Asset Name yang ditolak batas laju tidak menampilkan pesan dan field tetap netral

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Paksa respons pembacaan keunikan ditolak batas laju (429) lewat intercept jaringan
3. Ketik `Rate Limit Item {runId}-050` di field Asset Name lalu tunggu 1 detik
4. Verifikasi Field Asset Name berisi `Rate Limit Item {runId}-050` dan Popup Create tetap tampil
5. Verifikasi Tidak ada pesan inline, error state, maupun toast
6. Verifikasi Field Asset Name tetap netral tanpa border merah
7. Hapus intercept
8. Isi field wajib lain: Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
9. Klik `[Submit]`
10. Verifikasi Toast `Success, asset name has been created.` tampil

### TC-FA-FAAM-725 dan 726: Cek keunikan Code dan nama model yang ditolak batas laju

11. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
12. Paksa respons pembacaan keunikan ditolak batas laju (429) lewat intercept jaringan
13. Ketik `RATE-LIMIT` di field Code lalu tunggu 1 detik
14. Verifikasi Field Code berisi `RATE-LIMIT` dan Popup Create tetap tampil
15. Verifikasi Tidak ada pesan inline (termasuk `Code already exists`), error state, maupun toast
16. Verifikasi Field Code tetap netral tanpa border merah
17. Pilih Brand `Dell` sehingga baris Brand `Dell` tampil di Tabel Model/Type per Brand
18. Ketik `Rate Limit Model` pada input model baris `Dell` lalu tunggu 1 detik
19. Verifikasi Input model berisi `Rate Limit Model`
20. Verifikasi Tidak ada pesan inline (termasuk `Model name already exists`), error state, maupun toast
21. Verifikasi Input model tetap netral tanpa border merah
22. Hapus intercept
23. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Endpoint yang dicegat: pembacaan keunikan untuk Asset Name, Code, dan nama model (satu intercept per blok); payload tidak mengonsumsi state karena tidak ada Submit di blok Code dan model (bagian 8b butir 4). Jawaban 429 dipaksa lewat intercept, bukan flood nyata, jadi tidak ada counter server yang direset.
- Urutan TC dalam spec: TC-FA-FAAM-683 (berakhir Submit sukses dan menutup modal) lebih dahulu; TC-FA-FAAM-725 dan 726 berbagi satu pembukaan form karena keduanya hanya mengetik.
- TC-FA-FAAM-726 langkah memilih Brand dilakukan sesudah intercept dipasang pada TC-FA-FAAM-725; intercept yang sama tetap berlaku untuk pembacaan keunikan nama model.
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - Kelas TC-FA-FAAM-683, 725, 726 ditandai kelas c (flood rate-limit) pada pengelompokan, tetapi TC memaksa 429 lewat intercept jaringan pada satu sesi; spec ini memakai intercept FE+BE, bukan flood nyata.
