---
name: tagsamurai-e2e-audit
description: Audit hasil generate e2e TAG Samurai untuk satu suite: traceability TC granular → spec.md → web.test.ts, kepatuhan konvensi efisiensi dan data. Hanya melaporkan temuan, tidak memperbaiki.
---

# Audit E2E (report-only)

Skill ini hanya **melaporkan**. Jangan mengubah file apa pun, termasuk spec, script, dan TC granular. Tampilkan temuan ke user dan tunggu instruksi. Jangan langsung memperbaiki walau temuannya jelas.

Rujukan aturan: `docs/e2e-conventions.md`. Skill ini melengkapi `spectra lint`, yang hanya memeriksa format. Jalankan `spectra lint --strict specs/<Suite>` dan `pnpm type-check` dulu, lalu periksa hal-hal yang tidak dicakup linter.

## Input

Path suite (contoh `specs/GlobalSettings/User`) dan path `tc-[modul].md` sumbernya.

## Pemeriksaan

**A. Traceability (arah TC granular → spec)**
- Ekstrak semua id TC di `tc-[modul].md`. Untuk tiap id: apakah muncul di `sourceTc` spec mana pun, atau tercatat di `docs/coverage/<Suite>.md` beserta alasan tidak diotomasi?
- TC granular berprioritas P0/P1 yang tidak muncul di keduanya adalah temuan.
- Cek Changelog `tc-[modul].md` sebelum menyimpulkan ada id yang hilang (id yang sudah dihapus resmi bukan temuan).

**B. Traceability (arah spec → TC granular)**
- Setiap `sourceTc` menunjuk id yang benar-benar ada di `tc-[modul].md`.
- Isi spec sesuai TC sumbernya (role, precondition, langkah, expected result). Bandingkan per TC yang digabung. Langkah atau expected result yang hilang, ditambah, atau berubah makna adalah temuan.
- `priority` sesuai mapping bagian 8 konvensi (tertinggi dari TC sumber).
- `caseType` mengikuti aturan spec gabungan bagian 8 konvensi (jenis alur utama yang dominan). Jangan menandai temuan hanya karena TC sumber campuran jenisnya.
- `coverage.web` tidak dinilai terhadap `status`. Kolom itu hanya jenis pengujian, progres dibaca dari `status`.

**C. Spec → script**
- Tiap langkah `Verify ...` di spec.md punya assertion di `web.test.ts`, dan urutannya sama.
- Script tidak berisi aksi atau assertion yang tidak ada di spec.md.
- `it()` title = `title`. `@step` = `Step.*` (linter sudah memeriksa, konfirmasi hasilnya).
- Assertion tidak dangkal: bukan hanya cek elemen ada padahal expected result menyebut isi, badge, atau toast tertentu.

**D. Efisiensi dan independensi**
- Spec tidak bergantung pada data atau hasil spec lain (cari nama data yang dibuat di spec lain).
- Login dan seed dilakukan di hook, bukan diulang di tiap `it()`.
- Tidak ada dua spec dengan alur dan assert yang sama (duplikasi), dan tidak ada permutasi yang seharusnya digabung jadi loop atau parameter Step.
- Spec gabungan tidak melebihi ~12 langkah dan tidak mencampur role berbeda tanpa Step ganti akun.
- Setup yang dibutuhkan satu spec tidak ditaruh di `global-hooks`.

**E. Data**
- Tidak ada password, token, atau kredensial di spec, fixture, atau script.
- Data yang harus unik memakai suffix dinamis. Data yang dibuat spec dibersihkan di hook.
- Data pre-setup mengacu ke fixture yang cocok dengan tabel Data Uji Pre-setup di TC sumber.

**F. Kode**
- Tidak ada selector mentah di `web.test.ts`. Tidak ada xpath atau nth-child di Page Object.
- Tidak ada `sleep` atau jeda tetap, komentar di kode, import manual, atau `describe`/`test`.
- Struktur: suite di `specs/<ModulBesar>/<SubModul>/`, nama folder TC = id, penamaan entitas berprefix modul, tidak ada file di luar folder standar.

## Format laporan

1. Ringkasan: jumlah TC granular, jumlah spec, TC diotomasi / dilewati / belum tercakup, hasil lint dan type-check.
2. Tabel temuan, diurutkan dari yang paling berat: `No` | `Kategori (A-F)` | `Spec/TC` | `Temuan` | `Bukti (file:baris)` | `Saran`.
3. Bagian "Perlu keputusan" untuk hal yang tidak bisa disimpulkan dari file (contoh: TC sumber ambigu, atau selector belum ada di app).

Bedakan dua jenis penyebab pada tiap temuan: (1) kesalahan hasil generate, atau (2) kekurangan di TC sumber atau konvensi. Untuk jenis (2) arahkan ke perbaikan sumber, jangan ke spec.
