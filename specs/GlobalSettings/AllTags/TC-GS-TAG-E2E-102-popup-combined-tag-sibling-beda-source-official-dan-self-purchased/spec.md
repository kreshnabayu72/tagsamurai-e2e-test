---
id: TC-GS-TAG-E2E-102-popup-combined-tag-sibling-beda-source-official-dan-self-purchased
title: "Popup Combined TAG: Sibling Berbeda Source (Official dan Self-Purchased)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-378
coverage:
  web: automated
---

# Popup Combined TAG: Sibling Berbeda Source (Official dan Self-Purchased)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data uji: Seed Registri A (Client A, DD-01..DD-30). Fixture khusus TC-GS-TAG-378, di luar hitungan Seed Registri A, disisipkan backend di hook `before`: DD-60 RFID `E2801160600002054D8A0060` (Source `Official`, `Available`) berelasi combined dengan DD-61 NFC `04A224B2C15E90` (Source `Self-Purchased`, `Available`). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); seeding idempotent (dilewati bila sudah ada).
- Kemampuan teknis (disediakan tim FE/BE): sisip dan hapus fixture DD-60 dan DD-61 lewat backend, idempotent.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus fixture DD-60 dan DD-61.
- Suite serial (`parallel: false`). Spec tidak mengubah state global; baris fixture tidak ikut hitungan atau asersi kartu Seed Registri A.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-378: Popup Combined TAG memuat sibling berbeda Source

1. Ketik Search `E2801160600002054D8A0060`, tekan Enter
2. Verifikasi kolom Source baris DD-60 `Official`
3. Verifikasi ikon 🔗 tampil di sebelah Code baris DD-60
4. Klik ikon 🔗 pada baris DD-60
5. Verifikasi Popup Combined TAG baris DD-60 memuat sibling DD-61 (NFC, `04A224B2C15E90`)
6. Verifikasi tidak ada pesan atau penanda yang menyatakan perbedaan Source sebagai penghalang combined pada popup baris DD-60
7. Tutup popup
8. Ganti isi kotak search dengan `04A224B2C15E90`, tekan Enter
9. Verifikasi kolom Source baris DD-61 `Self-Purchased`
10. Verifikasi ikon 🔗 tampil di sebelah Code baris DD-61
11. Klik ikon 🔗 pada baris DD-61
12. Verifikasi Popup Combined TAG baris DD-61 memuat sibling DD-60 (RFID, `E2801160600002054D8A0060`)
13. Verifikasi tidak ada pesan atau penanda yang menyatakan perbedaan Source sebagai penghalang combined pada popup baris DD-61
14. Tutup popup

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. TC-GS-TAG-378 hanya ada di spec ini; spec berdiri sendiri karena memakai fixture khusus (DD-60 dan DD-61) di luar Seed Registri A dan tidak mengubah data bersama.
- Spec 14 langkah, di bawah batas sekitar 35 langkah, satu kelas harness.
- Urutan langkah per baris (DD-60 lalu DD-61), bukan mengamati kedua baris sekaligus seperti langkah 1 TC: TC tidak menyebut cara menampilkan kedua baris bersamaan, sehingga tiap baris dicari lewat Search atas Code-nya agar tidak bergantung pada halaman atau urutan tabel. Klausa Expected a dan d dipecah satu `Verifikasi` per klausa dan per baris (S-01).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 8 (Search untuk menampilkan baris), langkah 7 dan 14 (menutup popup).
- Asersi tambahan di luar Expected TC: tidak ada. Langkah 5 dan 12 (popup memuat sibling) menjadi anchor positif untuk asersi absence langkah 6 dan 13 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-TAG-378 langkah 1 tidak menyebut cara menampilkan baris DD-60 dan DD-61 pada tabel; spec memakai Search atas Code tiap baris.
  - TC-GS-TAG-378 Expected d tidak menyebut teks pesan atau penanda yang dicari; spec mengasersi tidak adanya pesan atau penanda perbedaan Source pada isi popup.
  - TC-GS-TAG-378 tidak punya Post Condition.
